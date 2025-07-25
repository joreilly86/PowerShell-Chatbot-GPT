# grok.py
from openai import OpenAI
from .chatbot_base import BaseChatbot

class GrokChatbot(BaseChatbot):
    def __init__(self):
        super().__init__(
            api_key_name="GROK_API_KEY",
            model_env_name="GROK_MODEL",
            api_base_url="https://api.x.ai/v1"
        )

    def _initialize_client(self):
        return OpenAI(api_key=self.api_key, base_url=self.api_base_url)

    def _get_response(self):
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=self.messages,
            stream=False,
        )
        return response.choices[0].message.content.strip()

if __name__ == "__main__":
    try:
        chatbot = GrokChatbot()
        chatbot.run()
    except (ValueError, ImportError) as e:
        print(f"[Error] {e}")