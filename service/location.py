from repositories.location import LocationRepository


class LocationService:
    def __init__(self, repository: LocationRepository):
        self.repository = repository

    async def save_user_location(self, user_name: str, location: str):
        await self.repository.store_location(user_name, location)

    async def retrieve_latest_location(self, user_name: str):
        return await self.repository.get_latest_location(user_name)
