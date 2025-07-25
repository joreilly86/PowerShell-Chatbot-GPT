# gem.py
import sys
import pyperclip
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

    def run(self):
        """
        Override the base run method to handle Gemini's unique chat state.
        """
        print(f"Chatbot is ready. Using model: {self.model_name}")
        print("Type 'exit' or 'quit' to end the session.")

        while True:
            try:
                print("You (Type a message, or type 'PASTE' to enter multi-line mode):")
                first_line = sys.stdin.readline().strip()

                if first_line.lower() in ["exit", "quit"]:
                    print("\nGoodbye!")
                    break

                if first_line.lower() == "paste":
                    print("(Multi-line mode: Paste your text now, then type 'ENDPASTE' on a new line and press Enter)")
                    user_input_lines = []
                    while True:
                        line = sys.stdin.readline()
                        if line.strip().lower() == "endpaste":
                            break
                        user_input_lines.append(line)
                    user_input = "".join(user_input_lines).strip()
                else:
                    user_input = first_line

                if not user_input:
                    continue
                
                self.messages.append({"role": "user", "content": user_input})

                try:
                    print("\nAI is thinking...")
                    response_content = self._get_response()
                    
                    print("\nAI Response:\n")
                    print(response_content)
                    print()

                    pyperclip.copy(response_content)

                except Exception as e:
                    print(f"\n[Error during generation] {e}\n")

            except (EOFError, KeyboardInterrupt):
                print("\nGoodbye!")
                break

if __name__ == "__main__":
    try:
        chatbot = GeminiChatbot()
        chatbot.run()
    except (ValueError, ImportError) as e:
        print(f"[Error] {e}")
