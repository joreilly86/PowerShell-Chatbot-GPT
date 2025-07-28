# chatbot_base.py
import os
import sys
import pyperclip
from dotenv import load_dotenv

class BaseChatbot:
    """A base class for creating command-line chatbots."""

    def __init__(self, api_key_name, model_env_name, api_base_url=None):
        load_dotenv(override=True)
        
        self.api_key = os.getenv(api_key_name)
        if not self.api_key:
            raise ValueError(f"Configuration Error: {api_key_name} is not set in your .env file.")
        
        self.model_name = os.getenv(model_env_name)
        if not self.model_name:
            raise ValueError(f"Configuration Error: {model_env_name} is not set in your .env file.")

        self.api_base_url = api_base_url
        self.client = self._initialize_client()
        self.messages = [self._get_system_prompt()]

    def _initialize_client(self):
        """Initializes the API client. This should be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement _initialize_client.")

    def _get_system_prompt(self):
        """Returns the system prompt. This can be overridden by subclasses."""
        return {
            "role": "system",
            "content": (
                "You are a helpful assistant. Provide clear, concise, and accurate "
                "information. Follow professional communication standards."
            ),
        }

    def run(self):
        """Runs the main chatbot loop."""
        print(f"Chatbot is ready. Using model: {self.model_name}")
        print("Type 'exit' or 'quit' to end the session.")
        
        while True:
            try:
                print("You:")
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
                    self.messages.append({"role": "assistant", "content": response_content})

                except Exception as e:
                    print(f"\n[Error during generation] {e}\n")
                    if self.messages and self.messages[-1]["role"] == "user":
                        self.messages.pop()

            except (EOFError, KeyboardInterrupt):
                print("\nGoodbye!")
                break
    
    def _get_response(self):
        """Sends messages to the model and gets a response."""
        raise NotImplementedError("Subclasses must implement _get_response.")
