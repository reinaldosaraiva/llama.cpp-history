import typer
from sqlmodel import Session, create_engine, select
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
        executions = session.exec(select(BenchmarkExecution)).all()
        for execution in executions:
            print(f"ID: {execution.id}")
            print(f"Model: {execution.model_name}")
            print(f"Timestamp: {execution.timestamp}")
            print(f"Parameters: {execution.parameters}")
            print(f"Performance Results: {execution.performance_results}")
            print(f"Tokens Predicted: {execution.tokens_predicted}")
            print(f"Tokens Evaluated: {execution.tokens_evaluated}")
            print(f"Generation Settings: {execution.generation_settings}")
            print("-" * 40)

if __name__ == "__main__":
    app()