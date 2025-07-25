# anthropic.py
from openai import OpenAI
from .chatbot_base import BaseChatbot

class AnthropicChatbot(BaseChatbot):
    def __init__(self):
        super().__init__(
            api_key_name="ANTHROPIC_API_KEY",
            model_env_name="ANTHROPIC_MODEL",
            api_base_url="https://api.anthropic.com/v1"
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
        chatbot = AnthropicChatbot()
        chatbot.run()
    except (ValueError, ImportError) as e:
        print(f"[Error] {e}")