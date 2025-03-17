import typer
from sqlmodel import Session, create_engine
from models import BenchmarkExecution
from datetime import datetime

app = typer.Typer()
engine = create_engine("sqlite:///llama_benchmark.db")

@app.command()
def add_execution(parameters: str, performance_results: str, model_name: str, tokens_predicted: int, tokens_evaluated: int, generation_settings: str):
    with Session(engine) as session:
        execution = BenchmarkExecution(
            parameters=parameters,
            performance_results=performance_results,
            model_name=model_name,
            tokens_predicted=tokens_predicted,
            tokens_evaluated=tokens_evaluated,
            generation_settings=generation_settings
        )
        session.add(execution)
        session.commit()
        print(f"Execution added with ID: {execution.id}")

@app.command()
def list_executions():
    with Session(engine) as session:
        executions = session.query(BenchmarkExecution).all()
        for execution in executions:
            print(f"ID: {execution.id}, Model: {execution.model_name}, Timestamp: {execution.timestamp}")

if __name__ == "__main__":
    app()