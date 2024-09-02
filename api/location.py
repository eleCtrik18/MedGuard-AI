from db.config import get_location_service
from fastapi import APIRouter, Depends, status, Response
from schema.common import APIResponse
from schema.location import LocationRequest
from service.location import LocationService

router = APIRouter()


@router.post("/save_location", response_model=APIResponse)
async def save_location(
    response: Response,
    location_data: LocationRequest,
    service: LocationService = Depends(get_location_service)
):
    try:
        await service.save_user_location(location_data.user_name, location_data.location)
        
        return APIResponse(
            success=True,
            message=f"Location saved for user {location_data.user_name}.",
            data={"user_name": location_data.user_name, "location": location_data.location}
        )

    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return APIResponse(
            success=False,
            message="An error occurred while processing your request",
            error=str(e)
        )

@router.get("/get_location/{user_name}", response_model=APIResponse)
async def get_latest_location(
    user_name: str,
    response: Response,
    service: LocationService = Depends(get_location_service)
):
    try:
        location = await service.retrieve_latest_location(user_name)
        
        if location:
            return APIResponse(
                success=True,
                message=f"Latest location retrieved for user {user_name}.",
                data=location
            )
        
        response.status_code = status.HTTP_404_NOT_FOUND
        return APIResponse(
            success=False,
            message=f"No location found for user {user_name}.",
            error="Location not found"
        )

    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return APIResponse(
            success=False,
            message="An error occurred while processing your request",
            error=str(e)
        )