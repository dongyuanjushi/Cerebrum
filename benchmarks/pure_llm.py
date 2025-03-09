from cerebrum.llm.apis import llm_chat

class PureLLM:
    def __init__(self):
        self.model_name = model_name

    def run(self, messages: list[dict]):
        return llm_chat("pure_llm", messages)
