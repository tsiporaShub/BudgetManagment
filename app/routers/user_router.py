from fastapi import APIRouter
import app.services.user_service as user_service
from app.models.user_model import User
from app.models.userDetails_model import UserDetails

user_router = APIRouter()


@user_router.post("/signup")
async def signup(user: User):
    return user_service.signup(user)


@user_router.post("/login")
async def login(userDetails: UserDetails):
    return user_service.login(userDetails)


@user_router.put("/updateDetails")
async def updateDetails(user: User):
    return user_service.updateDetails(user)
