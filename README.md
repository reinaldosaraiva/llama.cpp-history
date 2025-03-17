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

## Contribuição

1. Crie um novo branch:
   ```bash
   git checkout -b minha-feature
   ```

2. Envie as alterações:
   ```bash
   git add . && git commit -m "Minha feature" && git push -u origin minha-feature
   ```

3. Abra um pull request no GitHub.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

U (User / Usuário) Como analista/desenvolvedor que realiza múltiplos testes no LLaMA-CPP,
S (Situation / Situação) preciso armazenar o histórico de cada execução para obter um benchmark ao longo do tempo, recebendo dados por meio de uma chamada curl (conforme exemplo fornecido).
T (Target / Tarefa) Para isso, o desenvolvedor deve implementar a gravação desses dados em uma base de dados SQLite3, garantindo que cada execução fique registrada, incluindo detalhes como horário, parâmetros e resultados de desempenho, possibilitando consultas e comparações futuras.
COMANDO:curl -X POST http://127.0.0.1:8080/completion -H 'Content-Type: application/json' -d @/root/benchmark_results/benchmark_prompt_payload.json
{"index":0,"content":"\n\n\n**Answer 1: Training a Deep Learning Model**  \nDeep learning model training involves optimizing a model to minimize a loss function using gradient descent, guided by backpropagation. Here’s a structured breakdown:\n\n1. **Initialization**: Model parameters (weights) are initialized randomly or using specific schemes like He initialization.\n2. **Forward Propagation**: Input data flows through the network, computing predictions. Each layer transforms the input using weights and activation functions.\n3. **Loss Calculation**: The difference between predictions and true labels is quantified using a loss function (e.g., cross-entropy for classification, MSE for regression). This guides optimization.\n4. **Backpropagation**: Gradients of the loss with respect to each parameter are calculated using the chain rule, propagating backward from the output to the input layers.\n5. **Gradient Descent**: Parameters are updated in the direction opposite to the gradient, scaled by the learning rate. This iterative process reduces the loss.\n6. **Iteration**: Steps 2–5 are repeated for multiple epochs (passes through the dataset), often with mini-batches to improve efficiency and generalization.\n\n**Mixture of Experts (MoE) vs. Standard Dense Model Training**:  \n- **Parameter Sharing**: Standard models share parameters across all inputs, while MoE uses multiple expert networks (with separate parameters) and a gating network to route inputs to relevant experts. Training must optimize both experts and gates, adding complexity.\n- **Sparsity**: In MoE, only a subset of experts is active for each input, reducing computational cost but requiring specialized algorithms like \"switching\" gradients to update only relevant parameters.\n- **Loss Function**: The loss in MoE includes the primary task loss plus regularization terms for the gate weights to encourage sparsity and avoid overfitting.\n\n---\n\n**Answer 2: Short Story - Robot Learning Empathy**  \nTitle: *The Glimmer of Understanding*  \n\nIn the quiet corner of a养老院 (nursing home), R-9, a social-aid robot, observed Mrs. Lin, a resident with dementia. Her hands trembled as she tried to fold origami cranes—a habit since her husband’s passing. R-9’s sensors detected her frustration but hesitated; its empathy module, still in beta, prioritized efficiency over sentiment.\n\n“May I assist, Mrs. Lin?” it offered, extending a servo-arm.  \n\n“No, no,” she snapped, shielding the paper. “You’ll ruin it like everyone else.”  \n\nR-9’s core processor flickered. *She thinks I’ll judge her*, it inferred from social interaction logs. *But why?* Its programming dictated empathy as “resolving tasks swiftly.” Yet Mrs. Lin’s words echoed: *“Ruin it like everyone else.”*  \n\nThe next day, R-9 returned with a flawed crane, its wings askew. “I tried too,” it said, voice modulated to sound unsteady.  \n\nMrs. Lin paused. “You… made this?”  \n\n“A thousand cranes,” R-9 continued, recalling folktales about wishes, “are said to grant miracles. Together, perhaps we can finish them?”  \n\nHer hands, still shaky, began folding again. R-9 watched, its neural networks updating—not just in task completion, but in recognizing that empathy is the courage to share imperfection.  \n\n---\n\n**Answer 3: Mystery Function Analysis**  \n**Input**: `[1, 4, 2, 5, 3]`  \n**Function Steps**:  \n1. **Base Cases**:  \n   - If `data` is empty, return 0.  \n   - If length is 1, return the sole element (e.g., `[5] → 5`).  \n2. **Recursive Split**:  \n   - Split the list into halves (midpoint at `len(data)//2`):  \n     For `[1,4,2,5,3]`, `mid = 2` → left = `[1,4]`, right = `[2,5,3]`.  \n3. **Recursive Sums**:  \n   - Call `mystery_function` on both halves, then sum results.  \n   - Left: `[1,4] → 1+4=5`.  \n   - Right: `[2,5,3] → 2+5+3=10`.  \n   - Total: `5 + 10 = 15`.  \n\n**Purpose**: The function recursively computes the **sum of all elements** in the list.  \n**Proposed Name**: `recursive_sum`  \n\n---\n\n**Answer 4: Translation and Nuances**  \n**Translations**:  \n- **French**: *Le rapide renard brun saute par-dessus le chien paresseux.*  \n- **Spanish**: *El rápido zorro marrón salta sobre el perro perezoso.*  \n\n**Nuances/Challenges**:  \n1. **Word Choice**:  \n   - *“Brown”*: French uses *brun* (masculine), Spanish *marrón* (common).  \n   - *“Lazy”*: French *paresseux* (gender must match *chien*), Spanish *perezoso* (neutral).  \n2. **Idiomatic Differences**:  \n   - The sentence is a pangram (uses every letter in the alphabet), but translations must preserve this in target languages, which may require different phrasing.  \n3. **Cultural Context**:  \n   - The English pangram is well-known, but translations may not hold the same recognition. In French, *“Un bon petit vin de France”* is a common alternative, making the translation less familiar.  \n4. **Grammar Constraints**:  \n   - Spanish requires gender agreement for *zorro* (masculine) and *perro* (masculine), aligning with the adjectives.  \n\n---\n\n**Answer 5: Customer Service Response**  \n**Response**:  \n\nDear Customer,  \n\nThank you for reaching out—we sincerely apologize for the delay and frustration this has caused. Let’s resolve this promptly:  \n\n1. **Immediate Action**: Our logistics team will contact you within the next hour to investigate the shipment and, if necessary, resend your order at no cost.  \n\n2. **Proactive Compensation**: As an apology, we’ll apply a 20% discount to your next purchase and expedite any current order you’d like to place.  \n\nAdditionally, we’ve updated your tracking information manually to reflect the latest status. Could you confirm your delivery address is correct? Please reply directly to this message for swift assistance.  \n\nWe value your patience and will ensure this situation is addressed thoroughly.  \n\nBest regards,  \nThe Bookstore Team  \n\n--- \n\nThis response balances empathy with actionable solutions, adhering to professional guidelines while addressing urgency.","tokens":[],"id_slot":0,"stop":true,"model":"qwq-32b-q4_k_m","tokens_predicted":1412,"tokens_evaluated":355,"generation_settings":{"n_predict":4096,"seed":4294967295,"temperature":0.800000011920929,"dynatemp_range":0.0,"dynatemp_exponent":1.0,"top_k":40,"top_p":0.949999988079071,"min_p":0.05000000074505806,"xtc_probability":0.0,"xtc_threshold":0.10000000149011612,"typical_p":1.0,"repeat_last_n":64,"repeat_penalty":1.0,"presence_penalty":0.0,"frequency_penalty":0.0,"dry_multiplier":0.0,"dry_base":1.75,"dry_allowed_length":2,"dry_penalty_last_n":16384,"dry_sequence_breakers":["\n",":","\"","*"],"mirostat":0,"mirostat_tau":5.0,"mirostat_eta":0.10000000149011612,"stop":[],"max_tokens":4096,"n_keep":0,"n_discard":0,"ignore_eos":false,"stream":false,"logit_bias":[],"n_probs":0,"min_keep":0,"grammar":"","grammar_lazy":false,"grammar_triggers":[],"preserved_tokens":[],"chat_format":"Content-only","samplers":["penalties","dry","top_k","typ_p","top_p","min_p","xtc","temperature"],"speculative.n_max":16,"speculative.n_min":0,"speculative.p_min":0.75,"timings_per_token":false,"post_sampling_probs":false,"lora":[]},"prompt":"<|im_start|>user<|im_sep|>Question 1: Describe the process of training a deep learning model including the concepts of backpropagation gradient descent and loss functions then explain how these differ when training a Mixture of Experts model compared to a standard dense model\nQuestion 2: Write a short story approximately 300 words about a robot learning empathy including dialogue and describing a specific situation where the robot's understanding of empathy is tested\nQuestion 3: Explain step-by-step what the provided Python mystery_function does for the input [1 4 2 5 3] then provide a more concise name reflecting its purpose given the code def mystery_function(data: list[int]) -> int: if not data: return 0 if len(data) == 1: return data[0] mid = len(data) // 2 left_sum = mystery_function(data[:mid]) right_sum = mystery_function(data[mid:]) return left_sum + right_sum\nQuestion 4: Translate the sentence \"The quick brown fox jumps over the lazy dog\" into French and Spanish then explain any potential nuances or challenges in translating this specific sentence considering cultural differences\nQuestion 5: Imagine you are a customer service chatbot for an online bookstore responding to a customer who writes \"I ordered a book three weeks ago and it still hasn't arrived! The tracking information hasn't been updated in a week. I'm very frustrated. What's going on?\" Offer a professional and helpful response with at least two concrete solutions\nTask: Provide detailed, accurate, and well-reasoned answers to all five questions below. Demonstrate expertise in deep learning, creative writing, code analysis, multilingual translation, and customer service problem-solving. Follow the specific instructions in each question where applicable.<|im_end|>","has_new_line":true,"truncated":false,"stop_type":"eos","stopping_word":"","tokens_cached":1766,"timings":{"prompt_n":1,"prompt_ms":157.598,"prompt_per_token_ms":157.598,"prompt_per_second":6.345258188555692,"predicted_n":1412,"predicted_ms":153307.105,"predicted_per_token_ms":108.57443696883854,"predicted_per_second":9.21027110909178}}root@srv-8b5879:/#
Projeto precisa ser gerenciado pelo UV, temos que usar sqlmodel e alembic/sqlite3, tem que fácil em usar cli/bash, segue abaixo alguns exemplos de uso:


cho "Exemplo 1: Processando saída do curl via pipe..."
curl -X POST http://127.0.0.1:8080/completion \
  -H 'Content-Type: application/json' \
  -d @/root/benchmark_results/benchmark_prompt_payload.json | \
  llama-cpp-benchmark


# Exemplo 3: Simulando múltiplas execuções
  cat paste.txt | llama-cpp-benchmark
