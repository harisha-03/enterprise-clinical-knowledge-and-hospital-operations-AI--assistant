import requests


class OllamaLLM:

    def __init__(self):

        self.url = "http://localhost:11434/api/generate"

        self.model = "qwen2.5:3b"

    def generate(self, prompt: str):

        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]