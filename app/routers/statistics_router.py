from fastapi import APIRouter
import app.services.statistics_service as statistics_service

statistics_router = APIRouter()


@statistics_router.get("/users_balance")
async def users_balance():
    return await statistics_service.get_users_balance()
