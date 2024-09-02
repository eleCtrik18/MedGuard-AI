from db.config import get_location_service, get_qdrant_service
from fastapi import APIRouter, Depends, status, Response
from schema.common import APIResponse
from schema.location import LocationRequest
from schema.query_schema import QueryRequest
from service.location import LocationService
from service.query_service import QdrantService

router = APIRouter()

@router.post("/handle_query", response_model=APIResponse)
async def handle_query(
    response: Response,
    request_data: QueryRequest,
    service: QdrantService = Depends(get_qdrant_service)
):
    try:
        if request_data.query_type == "message":
            # await service.store_message(request_data.query_details)
            return APIResponse(
                success=True,
                message="Thanks for the message, we will forward it to Dr. Adrin",
                data={"message": request_data.query_details}
            )
        elif request_data.query_type == "emergency":
            instructions = await service.find_closest_instruction(query=request_data.query_details)
            if instructions:
                return APIResponse(
                    success=True,
                    message="Emergency instructions found",
                    data={"instruction": instructions}
                )
            response.status_code = status.HTTP_404_NOT_FOUND
            return APIResponse(
                success=False,
                message="No matching instruction found",
                error="Instruction not found"
            )
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return APIResponse(
                success=False,
                message="Invalid query type",
                error="Query type must be either 'emergency' or 'message'"
            )
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return APIResponse(
            success=False,
            message="An error occurred while processing your request",
            error=str(e)
        )
