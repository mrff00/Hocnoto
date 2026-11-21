class LLMUnavailable(Exception):
    """Raised when the LLM could not produce an answer (busy, blocked, empty...)."""


class LLMConfigError(Exception):
    """Raised when the LLM is set up wrongly (missing key, bad model name...)."""


class LLMClient:
    def generate(self, prompt: str) -> str:
        raise NotImplementedError