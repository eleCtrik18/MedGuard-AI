from repositories.query_repo import QdrantRepository

class QdrantService:
    def __init__(self, repository: QdrantRepository):
        self.repository = repository

    async def find_closest_instruction(self, query: str):
        return await self.repository.find_closest_instruction(query)

    # async def store_message(self, message: str):
    #     await self.repository.store_message(message)

    # async def get_latest_message(self):
    #     return await self.repository.get_latest_message()
