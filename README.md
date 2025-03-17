# LLaMA.cpp History

Este projeto permite armazenar e consultar o histórico de execuções de benchmarks do LLaMA-CPP em um banco de dados SQLite3. Ele utiliza `sqlmodel` para gerenciar o banco de dados e `uv` para gerenciar dependências.

## Configuração do Ambiente

1. **Instale o `uv`** (se ainda não estiver instalado):
   ```bash
   pip3 install uv
   ```

2. **Instale as dependências**:
   ```bash
   uv pip install -r requirements.in
   ```

3. **Configure o banco de dados**:
   - O banco de dados SQLite será criado automaticamente na primeira execução.

## Como Usar

### Adicionar uma Execução de Benchmark

Use o CLI para adicionar uma nova execução de benchmark:
```bash
python3 cli.py add-execution \
  --parameters '{"param1": "value1"}' \
  --performance-results '{"result1": "value1"}' \
  --model-name "model1" \
  --tokens-predicted 100 \
  --tokens-evaluated 50 \
  --generation-settings '{"setting1": "value1"}'
```

### Listar Execuções

Para listar todas as execuções armazenadas:
```bash
python3 cli.py list-executions
```

### Exemplo Completo

1. Execute um benchmark e capture a saída:
   ```bash
   curl -X POST http://127.0.0.1:8080/completion -H 'Content-Type: application/json' -d @/root/benchmark_results/benchmark_prompt_payload.json | python llm-benchmark.py
   ```

   Ou, se você já tiver um arquivo de saída:
   ```bash
   cat output.json | python llm-benchmark.py
   ```

2. Consulte o histórico:
   ```bash
   python3 cli.py list-executions
   ```

## Estrutura do Banco de Dados

O banco de dados SQLite (`llama_benchmark.db`) contém a tabela `benchmarkexecution` com os seguintes campos:
- `id`: Identificador único da execução.
- `timestamp`: Data e hora da execução.
- `parameters`: Parâmetros usados no benchmark.
- `performance_results`: Resultados de desempenho.
- `model_name`: Nome do modelo usado.
- `tokens_predicted`: Número de tokens previstos.
- `tokens_evaluated`: Número de tokens avaliados.
- `generation_settings`: Configurações de geração.



## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).



