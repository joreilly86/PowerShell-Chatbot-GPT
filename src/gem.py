# gem.py
import google.generativeai as genai
from .chatbot_base import BaseChatbot

class GeminiChatbot(BaseChatbot):
    def __init__(self):
        super().__init__(
            api_key_name="GOOGLE_API_KEY",
            model_env_name="GEMINI_MODEL"
        )
        # The chat history is managed differently in the Gemini SDK
        self.chat = self._initialize_chat()
        self.messages = [] # Base class history not used directly

    def _initialize_client(self):
        # The client is configured globally for this SDK
        genai.configure(api_key=self.api_key)
        return genai.GenerativeModel(
            model_name=self.model_name,
            system_instruction=self._get_system_prompt()["content"]
        )

    def _initialize_chat(self):
        return self.client.start_chat(history=[])

    def _get_system_prompt(self):
        return {
            "role": "system",
            "content": (
                "You are a technical AI assistant focused on engineering and scientific topics. "
                "Provide clear, concise, and accurate information."
            ),
        }

    def _get_response(self):
        # The user_input is the last message in the base class's list
        user_input = self.messages[-1]["content"]
        response = self.chat.send_message(user_input)
        return response.text.strip()


if __name__ == "__main__":
    try:
        chatbot = GeminiChatbot()
        chatbot.run()
    except (ValueError, ImportError) as e:
        print(f"[Error] {e}")
