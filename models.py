from sqlmodel import SQLModel, Field
from datetime import datetime

class BenchmarkExecution(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    parameters: str
    performance_results: str
    model_name: str
    tokens_predicted: int
    tokens_evaluated: int
    generation_settings: str