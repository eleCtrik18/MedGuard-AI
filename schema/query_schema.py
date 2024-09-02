from pydantic import BaseModel


class QueryRequest(BaseModel):
    query_type: str
    query_details: str