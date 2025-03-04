from typing import Annotated, Any, Dict, List
from fastapi import APIRouter, Depends, HTTPException
from controller.utils.current_user import get_current_user
from sqlalchemy.orm import Session
from datetime import datetime
from database import get_db

from models.roleReview import CoreFocusArea, CriticalActivities

from routes.coreFocusArea.schema.corefocusarea_schema import (
    CoreFocusAreaResponse,
    CoreFocusAreaUpdate,
    CoreFocusAreaCreate
)
# UserDependency = Annotated[dict, Depends(get_current_user)]
router = APIRouter()

UserDependency = Annotated[dict, Depends(get_current_user)]
# @router.post("/core_focus_areas/", response_model=List[CoreFocusAreaResponse])
# def create_core_focus_area(core_focus_area: List[CoreFocusAreaCreate], db: Session = Depends(get_db)):
#     # Delete existing records for the same user_ids
#     user_ids = [data.user_id for data in core_focus_area]
#     db.query(CoreFocusArea).filter(CoreFocusArea.user_id.in_(user_ids)).delete(synchronize_session=False)

#     # Add new records
#     new_areas = []
#     for data in core_focus_area:
#         # If id is not provided, create a new entry
#             new_area = CoreFocusArea(
#                 area=data.area,
#                 user_id=data.user_id,
#                 time_spent=data.time_spent,
#                 importance=data.importance,

#                 # created_at=datetime.now(),
#                 # updated_at=datetime.now()
#             )
#             new_areas.append(new_area)

#     db.add_all(new_areas)
#     db.commit()

#     return new_areas


@router.post("/core_focus_areas/", response_model=List[CoreFocusAreaResponse])
def create_or_update_core_focus_area(core_focus_area: List[CoreFocusAreaCreate], db: Session = Depends(get_db)):
    # Extract user_ids to process the update
    user_ids = [data.user_id for data in core_focus_area]

    # Fetch existing core focus areas for these user_ids
    existing_areas = db.query(CoreFocusArea).filter(CoreFocusArea.user_id.in_(user_ids)).all()

    # Prepare to track which records need to be updated or added
    updated_areas = []

    # Map existing areas by user_id and area for fast lookup
    existing_areas_map = {
        (area.user_id, area.area): area for area in existing_areas
    }

    for data in core_focus_area:
        # Check if the current input record exists
        existing_area = existing_areas_map.get((data.user_id, data.area))

        if existing_area:
            # If record exists, update it
            existing_area.time_spent = data.time_spent
            existing_area.importance = data.importance
            db.add(existing_area)
            updated_areas.append(existing_area)
            # Remove the updated record from the map (to track removal later)
            del existing_areas_map[(data.user_id, data.area)]
        else:
            # If no record exists, create a new one
            new_area = CoreFocusArea(
                area=data.area,
                user_id=data.user_id,
                time_spent=data.time_spent,
                importance=data.importance,
            )
            db.add(new_area)
            updated_areas.append(new_area)

    # Now, delete related critical activities before removing the core focus areas
    for area in existing_areas_map.values():
        # Delete critical activities related to the core focus area
        db.query(CriticalActivities).filter(CriticalActivities.core_focus_area_id == area.id).delete(synchronize_session=False)

    # Now, remove any remaining records from the map (these were not included in the new input)
    for key, area in existing_areas_map.items():
        db.delete(area)  # This record needs to be removed

    db.commit()

    return updated_areas





@router.put("/core_focus_areas/{user_id}", response_model=List[CoreFocusAreaUpdate])
def update_core_focus_area(user_id: int, core_focus_area: List[CoreFocusAreaUpdate], db: Session = Depends(get_db)):
    # Fetch all CoreFocusArea records for the given user
    db_core_focus_areas = db.query(CoreFocusArea).filter(CoreFocusArea.user_id == user_id).all()
    
    if not db_core_focus_areas:
        raise HTTPException(status_code=404, detail="CoreFocusArea not found for this user")

    # Create a dictionary to map the CoreFocusArea id to the object for faster lookup
    core_focus_area_map = {item.id: item for item in db_core_focus_areas}

    # Iterate over each update item in the input list
    for update_item in core_focus_area:
        # Check if the CoreFocusArea with the provided id exists in the fetched records
        db_item = core_focus_area_map.get(update_item.id)

        if db_item:
            # Update the fields that are present in the request
            update_data = update_item.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_item, key, value)

            # Commit changes to the database
            db.commit()
            db.refresh(db_item)
        else:
            raise HTTPException(status_code=404, detail=f"CoreFocusArea with id {update_item.id} not found for this user")

    # Return the updated list of CoreFocusArea objects
    return db_core_focus_areas

@router.get("/core_focus_areas/{user_id}", response_model=List[CoreFocusAreaCreate])
def read_core_focus_areas_by_user_id(user_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    core_focus_areas = db.query(CoreFocusArea).filter(CoreFocusArea.user_id == user_id).offset(skip).limit(limit).all()
    if not core_focus_areas:
        raise HTTPException(status_code=404, detail="Core Focus Areas not found")
    return core_focus_areas



@router.get("/core_focus_areas/time_spent/{user_id}", response_model=List[Dict[str, Any]])
def get_time_spent(user_id: int, db: Session = Depends(get_db)):
    core_focus_areas = db.query(CoreFocusArea).filter(CoreFocusArea.user_id == user_id).all()
   
    result = [
        {"area": area.area, "time_spent": area.time_spent}
        for area in core_focus_areas
    ]

    return result

@router.get("/core_focus_areas/importance/{user_id}", response_model=List[Dict[str, Any]])
def get_importance(user_id: int, db: Session = Depends(get_db)):
    core_focus_areas = db.query(CoreFocusArea).filter(CoreFocusArea.user_id == user_id).all()
   
    result = [
        {"area": area.area, "importance": area.importance}
        for area in core_focus_areas
    ]

    return result



