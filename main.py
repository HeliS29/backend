import os
from fastapi import FastAPI
from database import Base, engine
from routes.auth import user_routes, auth_routes
from routes.profile import profile_routes
from routes.roleReview import roleReview_routes
from routes.coreFocusArea import coreFocusArea_routes
from routes.coreFocusArea import coreFocusArea_routes
from fastapi.middleware.cors import CORSMiddleware
from routes.criticalactivities import criticalActivities_routes
from routes.report import report_routes
from routes.emailRequest import emailRequest
from routes.manager import manager_routes
from routes.comments import comments_routes
from routes.history_routes import history_routes
from fastapi.security import OAuth2PasswordBearer
app = FastAPI(
    docs_url=os.environ.get("DOCS_URL", "/docs"),  # Enable / Disable Swagger UI
    redoc_url=os.environ.get("REDOC_URL", "/documentation"),  # Enable / Disable ReDoc UI
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},  # hide schemas at bottom of Docs
)
from fastapi.staticfiles import StaticFiles
# JWT_BEARER = OAuth2PasswordBearer(tokenUrl="/auth/login")


app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://192.168.3.19:49340"],  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)
Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "Hello World"}

app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(auth_routes.router, prefix="/auth", tags=["Authentication"])
app.include_router(profile_routes.router, prefix="/profile", tags=["Profile"])
app.include_router(roleReview_routes.router, prefix="/roleReview", tags=["roleReview"])
app.include_router(coreFocusArea_routes.router, prefix="/coreFocusArea", tags=["coreFocusArea"])
app.include_router(criticalActivities_routes.router, prefix="/criticalactivities", tags=["criticalactivities"])
app.include_router(report_routes.router, prefix="/report", tags=["Report"])
app.include_router(emailRequest.router, prefix="/email", tags=["Email"])
app.include_router(manager_routes.router, prefix="/manager", tags=["Manager"])
app.include_router(comments_routes.router, prefix="/comment", tags=["Comment"])
app.include_router(history_routes.router, prefix="/history", tags=["CHistorymment"])