# bot.py
from openai import OpenAI
from .chatbot_base import BaseChatbot

class OpenAIChatbot(BaseChatbot):
    def __init__(self):
        super().__init__(
            api_key_name="OPENAI_API_KEY",
            model_env_name="OPENAI_MODEL"
        )

    def _initialize_client(self):
        return OpenAI(api_key=self.api_key)

    def _get_response(self):
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=self.messages,
            stream=False,
        )
        return response.choices[0].message.content.strip()

if __name__ == "__main__":
    try:
        chatbot = OpenAIChatbot()
        chatbot.run()
    except (ValueError, ImportError) as e:
        print(f"[Error] {e}")