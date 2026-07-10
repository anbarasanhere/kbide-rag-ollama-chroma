# temporary file to test the service

from services.ollama_service import OllamaService

llm = OllamaService()

response = llm.generate_response("What is the capital of France?")

print(response)

