from pydantic import BaseModel

class LocationRequest(BaseModel):
    current_location: str