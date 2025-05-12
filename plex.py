# Required libraries: pip install openai python-dotenv pyperclip
import os

import pyperclip
from dotenv import load_dotenv
from openai import OpenAI  # Use the OpenAI library

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
# Set the Perplexity model name. Uses PERPLEXITY_MODEL from .env,
# otherwise defaults to "sonar-pro" as shown in Perplexity's example.
# Check Perplexity's API documentation for other available models (e.g., sonar-small-32k).
DEFAULT_MODEL = "sonar-pro"
model_name = os.getenv("PERPLEXITY_MODEL", DEFAULT_MODEL)

# Get the Perplexity API key from environment variables
# Ensure you have set this in your .env file
api_key = os.getenv("PERPLEXITY_API_KEY")
if not api_key:
    raise ValueError("PERPLEXITY_API_KEY is not set. Please add it to your .env file.")

# Perplexity API base URL
perplexity_base_url = "https://api.perplexity.ai"

# Initialize the OpenAI client, but point it to Perplexity's API endpoint
try:
    client = OpenAI(api_key=api_key, base_url=perplexity_base_url)
    # You can optionally add other client configurations like timeout here
    # client = OpenAI(api_key=api_key, base_url=perplexity_base_url, timeout=30.0)
except Exception as e:
    print(f"[Error] Failed to initialize OpenAI client for Perplexity: {e}")
    exit()

# --- System Prompt ---
# Generic technical system prompt (suitable for general use)
# Note: Perplexity models often incorporate web search; their citation behavior might differ.
system_prompt_content = (
    "You are a helpful and thorough AI assistant. Provide clear, concise, and accurate "
    "information, leveraging search capabilities when necessary. Follow professional "
    "communication standards. Prioritize precision and efficiency in your responses."
    # "Cite sources where appropriate." # Keep or remove based on observed behavior
)


def run_chatbot():
    """Runs the chatbot using Perplexity Sonar API via OpenAI library."""
    print("Chatbot is ready. Type 'exit' or 'quit' to end the session.\n")
    print(
        f"Hello, I am using the Perplexity {model_name} model. How can I help you today?\n"
    )

    # Initialize message history using the OpenAI format
    messages = [
        {
            "role": "system",
            "content": system_prompt_content,
        }
    ]

    # --- Main Chat Loop ---
    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Add user message to the history list
        messages.append({"role": "user", "content": user_input})

        try:
            # Make the API call using the configured OpenAI client
            response = client.chat.completions.create(
                model=model_name,  # Specify the Perplexity model
                messages=messages,  # Pass the chat history
                stream=False,  # Get the full response at once
                # --- Optional Parameters ---
                # temperature=0.7,        # Adjust for creativity vs. determinism
                # max_tokens=1024,        # Limit response length if needed
            )

            # Extract the response content (using standard OpenAI response structure)
            if response.choices:
                response_content = response.choices[0].message.content.strip()
            else:
                response_content = (
                    "[Error] No response received from API."  # Handle empty choices
                )

            # Output AI response (screen reader friendly)
            print("\nAI Response:\n")
            print(response_content)
            print()

            # Copy the response content to the clipboard
            try:
                pyperclip.copy(response_content)
            except pyperclip.PyperclipException as clip_err:
                print(f"[Clipboard Error] Could not copy to clipboard: {clip_err}\n")

            # Add the assistant's response to the history for context
            messages.append({"role": "assistant", "content": response_content})

            # --- Optional: Limit History Size ---
            # Keep the system prompt + the last N user/assistant pairs
            # Adjust MAX_HISTORY_PAIRS as needed
            # MAX_HISTORY_PAIRS = 10
            # max_messages = 1 + (MAX_HISTORY_PAIRS * 2) # System + N pairs
            # if len(messages) > max_messages:
            #    # Keep the system prompt (index 0) and the latest messages
            #    messages = [messages[0]] + messages[-max_messages+1:]

        except Exception as e:
            print(f"\n[Error during generation] {e}\n")
            # If an error occurred, remove the last user message we added,
            # so we don't keep trying it in a broken state.
            if messages and messages[-1]["role"] == "user":
                messages.pop()


if __name__ == "__main__":
    run_chatbot()
