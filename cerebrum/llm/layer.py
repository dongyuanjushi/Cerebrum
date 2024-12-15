from dataclasses import dataclass
from typing import List
# @dataclass
# class LLMLayer:
#     llm_name: str
#     max_gpu_memory: dict | None = None
#     eval_device: str = "cuda:0"
#     max_new_tokens: int = 2048
#     log_mode: str = "console"
#     llm_backend: str = "default"
@dataclass
class LLMItem:
    llm_name: str
    max_gpu_memory: dict | None = None
    eval_device: str = "cuda:0"
    max_new_tokens: int = 2048
    log_mode: str = "console"
    llm_backend: str = "default"

@dataclass
class LLMLayer:
    llms: List[LLMItem]

    def __post_init__(self):
        if not self.llms:
            raise ValueError("LLMLayer must contain at least one LLM")