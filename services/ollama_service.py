from ollama import chat 

class OllamaService:
    '''Handles Communication with the local ollama model.
    '''
    def __init__(self, model_name: str = "qwen2.5:3b"):
        self.model_name = model_name

    def generate_response(self, prompt: str) -> str:
        '''Send a Prompt to the ollama model and return the response.
        '''
        response = chat(self.model_name,
                        messages = [{
                            "role": "user", "content": prompt
            }])
        return response['message']['content']