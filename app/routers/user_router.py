from fastapi import APIRouter, Request
import app.services.user_service as user_service
from app.models.user_model import User
from app.models.userDetails_model import UserDetails
from utils.logger import log_request

user_router = APIRouter()


@user_router.post("/signup")
@log_request
async def signup(user: User, request: Request):
    return await user_service.signup(user)


@user_router.post("/login")
@log_request
async def login(userDetails: UserDetails, request: Request):
    return await user_service.login(userDetails)


@user_router.put("/{user_id}")
@log_request
async def updateDetails(user_id, user: User, request: Request):
    return await user_service.updateDetails(user_id, user)
