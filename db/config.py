from qdrant_client import QdrantClient
from repositories.location import LocationRepository
from repositories.query_repo import QdrantRepository
from sentence_transformers import SentenceTransformer
from service.location import LocationService
from service.query_service import QdrantService
from fastapi import Depends

class QdrantConfig:
    def __init__(self, host: str = "localhost", port: int = 6333, prefer_grpc: bool = False):
        self.client = QdrantClient(host=host, port=port, prefer_grpc=prefer_grpc)
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def get_client(self) -> QdrantClient:
        return self.client

    def get_model(self) -> SentenceTransformer:
        return self.model


def get_qdrant_repository(config: QdrantConfig = Depends()) -> QdrantRepository:
    return QdrantRepository(client=config.get_client(), model=config.get_model())

def get_qdrant_service(repository: QdrantRepository = Depends(get_qdrant_repository)) -> QdrantService:
    return QdrantService(repository)    

def get_location_repository(config: QdrantConfig = Depends()) -> LocationRepository:
    return LocationRepository(client=config.get_client(), model=config.get_model())

def get_location_service(repository: LocationRepository = Depends(get_location_repository)) -> LocationService:
    return LocationService(repository)