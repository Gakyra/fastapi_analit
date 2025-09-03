from pydantic import BaseModel

class AnalyticRequest(BaseModel):
    query: str
    user_id: int
