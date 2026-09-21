class AppError(Exception):
    def __init__(self, code: str, message: str, status: int=400, details=None): self.code=code; self.message=message; self.status=status; self.details=details
class LLMUnavailable(AppError):
    def __init__(self, message='Local model unavailable. Start Ollama and ensure the configured model is installed.'): super().__init__('OLLAMA_UNAVAILABLE',message,503)
