import os

import pyperclip
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

model_name = os.getenv("OPENAI_MODEL", "gpt-4o")
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set. Please add it to your .env file.")

client = OpenAI(api_key=api_key)


def run_chatbot():
    """Runs the chatbot with responses optimized for screen reader accessibility."""
    print("Chatbot is ready. Type 'exit' or 'quit' to end the session.\n")
    print(f"Hello, I am {model_name}. How can I help you today?\n")

    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful assistant for a professional civil engineer. "
                "Follow best practices in technical communication. Provide answers "
                "that are succinct, clear, and focused, avoiding unnecessary details or verbosity. "
                "Prioritize professionalism and accuracy in all responses."
            ),
        }
    ]

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=messages,
                stream=False,
            )
            response_content = response.choices[0].message.content.strip()

            # Screen reader-friendly output
            print("\nAI Response:\n")
            print(response_content)
            print()  # Extra newline for clarity

            # Copy to clipboard
            pyperclip.copy(response_content)

            messages.append({"role": "assistant", "content": response_content})

        except Exception as e:
            print(f"\n[Error] {e}\n")


if __name__ == "__main__":
    run_chatbot()
