python -m benchmarks.humaneval.inference \
  --data_name openai/openai_humaneval \
  --split test \
  --output_file benchmarks/humaneval/llm_eval_prediction.json \
  --on_aios \
  --agent_type llm

# evaluate_functional_correctness benchmarks/humaneval/llm_eval_prediction.json