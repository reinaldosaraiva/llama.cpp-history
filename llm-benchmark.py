import sys
import json
from sqlmodel import Session, create_engine
from models import BenchmarkExecution

# Configuração do banco de dados
engine = create_engine("sqlite:///llama_benchmark.db")

def process_benchmark_output(output):
    try:
        data = json.loads(output)
        execution = BenchmarkExecution(
            parameters=json.dumps({"content": data.get("content", "")}),
            performance_results=json.dumps({"tokens_predicted": data.get("tokens_predicted", 0), "tokens_evaluated": data.get("tokens_evaluated", 0)}),
            model_name=data.get("model", "unknown"),
            tokens_predicted=data.get("tokens_predicted", 0),
            tokens_evaluated=data.get("tokens_evaluated", 0),
            generation_settings=json.dumps(data.get("generation_settings", {}))
        )
        with Session(engine) as session:
            session.add(execution)
            session.commit()
            print(f"Execution added with ID: {execution.id}")
    except json.JSONDecodeError:
        print("Error: Invalid JSON output from benchmark.")
        sys.exit(1)

if __name__ == "__main__":
    # Lê a saída do stdin (pipe do curl ou cat)
    output = sys.stdin.read()
    process_benchmark_output(output)