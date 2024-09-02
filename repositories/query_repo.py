import random
import uuid
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from qdrant_client.http.models import PointStruct, VectorParams
from constants.instructions import EMERGENCY_INSTRUCTIONS  

class QdrantRepository:
    def __init__(self, client: QdrantClient, model: SentenceTransformer):
        self.client = client
        self.model = model
        self.collection_name = "emergencies"

        # Store the instructions in Qdrant when the repository is initialized
        self._store_emergency_instructions()

    def _store_emergency_instructions(self):
        vectors = []
        point_id = 0  # Initialize an integer ID

        for key, instructions in EMERGENCY_INSTRUCTIONS.items():
            for instruction in instructions:
                vector = self.model.encode(key)
                vectors.append(PointStruct(
                    id=point_id,  # Use an integer ID
                    vector=vector,
                    payload={"description": key, "instruction": instruction}
                ))
                point_id += 1  # Increment the ID for each instruction
        
        vectors_config = VectorParams(
            size=len(vectors[0].vector),  # The size of the vectors
            distance="Cosine"  
        )

        self.client.recreate_collection(
            collection_name=self.collection_name, 
            vectors_config=vectors_config
        )

        self.client.upsert(
            collection_name=self.collection_name, 
            points=vectors
        )

    async def find_closest_instruction(self, query: str):
        query_vector = self.model.encode(query)

        # Search for the closest matching instructions
        results = self.client.search(
            collection_name="emergencies", 
            query_vector=query_vector,  
            limit=4  # Retrieve up to 4 matching instructions
        )

        if results:
            # Randomly select one of the matching instructions
            selected_instruction = random.choice(results).payload['instruction']
            return selected_instruction
        
        return None
