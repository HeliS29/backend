from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException
from controller.utils.current_user import get_current_user
from sqlalchemy.orm import Session
from database import get_db
from typing import Dict, List, Any
from models.roleReview import CriticalActivities,CoreFocusArea
from routes.criticalactivities.schema.criticalActivities_schema import (
    CriticalActivityCreate,
    CriticalActivityUpdate,
    CriticalActivityResponse,
)

router = APIRouter()


UserDependency = Annotated[dict, Depends(get_current_user)]
@router.post("/critical_activities/", response_model=List[CriticalActivityResponse])
def create_critical_activity(current_user:UserDependency,
    critical_activity: List[CriticalActivityCreate], db: Session = Depends(get_db)
):
    # Extract unique user IDs from the input data
    user_ids = [data.user_id for data in critical_activity]

    # Delete existing records for the same user IDs
    db.query(CriticalActivities).filter(CriticalActivities.user_id.in_(user_ids)).delete(synchronize_session=False)

    # Add new records
    new_activities = []
    for data in critical_activity:
        # If id is not provided, create a new entry
        new_activity = CriticalActivities(
            area=data.area,
            user_id=data.user_id,
            core_focus_area_id=data.core_focus_area_id,
            importance=data.importance,
            # created_at=datetime.now(),
            # updated_at=datetime.now()
        )
        new_activities.append(new_activity)

    db.add_all(new_activities)
    db.commit()

    return new_activities


@router.get("/critical_activities/", response_model=List[CriticalActivityResponse])
def get_all_critical_activities(current_user:UserDependency,db: Session = Depends(get_db)):
    activities = db.query(CriticalActivities).all()
    return activities

@router.get("/critical_activities/user/{user_id}", response_model=List[CriticalActivityResponse])
def get_critical_activities_by_user(current_user:UserDependency,user_id: int, db: Session = Depends(get_db)):
    activities = db.query(CriticalActivities).filter(CriticalActivities.user_id == user_id).all()
    if not activities:
        raise HTTPException(status_code=404, detail="No critical activities found for this user")
    return activities

from typing import List

@router.put("/critical_activities/{user_id}", response_model=List[CriticalActivityResponse])
def update_critical_activities(
    current_user:UserDependency,
    user_id: int, 
    activities_update: List[CriticalActivityUpdate], 
    db: Session = Depends(get_db)
):
    # Fetch the list of CriticalActivities by user_id
    db_activities = db.query(CriticalActivities).filter(CriticalActivities.user_id == user_id).all()

    if not db_activities:
        raise HTTPException(status_code=404, detail="No critical activities found for this user")

    updated_activities = []

    # Iterate over each update request in activities_update
    for update_item in activities_update:
        # Find the activity that matches the core_focus_area_id or critical activity id
        db_activity = next((activity for activity in db_activities if activity.id == update_item.core_focus_area_id), None)

        if db_activity:
            # Apply the updates
            for key, value in update_item.dict(exclude_unset=True).items():
                setattr(db_activity, key, value)
            
            db.commit()
            db.refresh(db_activity)
            updated_activities.append(db_activity)

    if not updated_activities:
        raise HTTPException(status_code=404, detail="No activities were updated")

    # Return the updated activities list
    return updated_activities


@router.get("/user_details/{user_id}", response_model=Dict[str, Any])
def get_user_details(current_user:UserDependency,user_id: int, db: Session = Depends(get_db)):
    # Fetch critical activities based on user_id
    critical_activities = (
        db.query(CriticalActivities)
        .filter(CriticalActivities.user_id == user_id)
        .all()
    )

    if not critical_activities:
        return {"message": f"This user has no critical activities."}

    result = []
    core_focus_area_ids = set()  # Use a set to keep track of unique core focus area IDs

    for ca in critical_activities:
        # Fetch core focus area details using core_focus_area_id
        core_focus_area = (
            db.query(CoreFocusArea)
            .filter(CoreFocusArea.id == ca.core_focus_area_id)
            .first()
        )

        if core_focus_area and core_focus_area.id not in core_focus_area_ids:
            core_focus_area_ids.add(core_focus_area.id)

            subtasks = (
                db.query(CriticalActivities)
                .filter(CriticalActivities.core_focus_area_id == core_focus_area.id)
                .all()
            )
            result.append({
                "core_focus_area": core_focus_area.area,
                "time_spent": core_focus_area.time_spent,
                "critical_activity": {
                    "subtasks": [{"area": st.area, "importance": st.importance} for st in subtasks]
                }
            })

    return {"user_id": user_id, "details": result}





# @router.post("/critical_activities/", response_model=List[CriticalActivityResponse])
# def create_critical_activity(
#     critical_activity: List[CriticalActivityCreate], db: Session = Depends(get_db)
# ):
#     db_critical_activity = [CriticalActivities(**area.dict()) for area in critical_activity]
#     db.add_all(db_critical_activity)
#     db.commit()
#     return db_critical_activity
    # new_activity = CriticalActivities(**critical_activity.dict())
    # db.add(new_activity)
    # db.commit()
    # db.refresh(new_activity)
    # return new_activity

# @router.get("/user_details/{user_id}", response_model=Dict[str, Any])
# def get_user_details(user_id: int, db: Session = Depends(get_db)):
#     # Fetch critical activities based on user_id
#     critical_activities = (
#         db.query(CriticalActivities)
#         .filter(CriticalActivities.user_id == user_id)
#         .all()
#     )

#     if not critical_activities:
#         return {"message": f"This user has no critical activities."}

#     result = []
#     for ca in critical_activities:
#         # Fetch core focus area details using core_focus_area_id
#         core_focus_area = (
#             db.query(CoreFocusArea)
#             .filter(CoreFocusArea.id == ca.core_focus_area_id)
#             .first()
#         )

#         if core_focus_area:
#             result.append({
#                 "core_focus_area": core_focus_area.area,
#                 "time_spent": core_focus_area.time_spent,
#                 "critical_activity": {
#                     "area": ca.area,
#                     "importance": ca.importance
#                 }
#             })

#     return {"user_id": user_id, "details": result}



