from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from qdrant_client.http.models import PointStruct, VectorParams
from datetime import datetime

class LocationRepository:
    def __init__(self, client: QdrantClient, model: SentenceTransformer):
        self.client = client
        self.model = model
        self.collection_name = "user_locations"

        # Initialize the location collection
        self._initialize_location_collection()

    def _initialize_location_collection(self):
        vectors_config = VectorParams(
            size=768,  # Assuming the vector size from your model
            distance="Cosine"  # Metric to use for vector similarity (can be "Euclidean", "Cosine", "Dot")
        )

        self.client.recreate_collection(
            collection_name=self.collection_name, 
            vectors_config=vectors_config
        )

    async def store_location(self, user_name: str, location: str):
        # Encode the username to generate a query vector
        vector = self.model.encode(user_name)  

        # Create a point with user location data and timestamp
        point = PointStruct(
            id=f"{user_name}:{datetime.utcnow().isoformat()}",  # Unique ID with username and timestamp
            vector=vector,
            payload={
                "user_name": user_name,
                "location": location,
                "timestamp": datetime.utcnow().isoformat()
            }
        )

        # Upsert the point to store or update the location data
        self.client.upsert(
            collection_name=self.collection_name,
            points=[point]
        )

    async def get_latest_location(self, user_name: str):
        query_vector = self.model.encode(user_name)
        
        # Search for the latest location of the user
        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            limit=1,
            with_payload=True,  # Retrieve payload with results
            sort_by="timestamp"  # Sort by timestamp to get the latest entry
        )
        
        if results:
            return results[0].payload  # Return the latest location data
        return None
