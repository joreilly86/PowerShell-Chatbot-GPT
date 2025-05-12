# Required libraries: pip install google-generativeai python-dotenv pyperclip
import os
import google.generativeai as genai
import pyperclip
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
# Set the model name. Uses GEMINI_MODEL from .env first, then GOOGLE_MODEL,
# otherwise defaults to the Gemini 2.5 Flash Preview model.
# You can set GEMINI_MODEL=gemini-2.5-pro-preview-05-06 in your .env
# file to use the Gemini 2.5 Pro Preview model instead.
DEFAULT_MODEL = "gemini-2.5-flash-preview-04-17"
model_name = os.getenv("GEMINI_MODEL") or os.getenv("GOOGLE_MODEL", DEFAULT_MODEL)

# Get the API key from environment variables
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY is not set. Please add it to your .env file.")

# Configure the Google Generative AI SDK
try:
    genai.configure(api_key=api_key)
except Exception as e:
    print(f"[Error] Failed to configure Google AI SDK: {e}")
    exit() # Exit if configuration fails

# --- System Prompt ---
# Revised system prompt for general technical use
system_prompt = (
    "You are a technical AI assistant focused on engineering and scientific topics. "
    "Provide clear, concise, and accurate information. Follow professional communication "
    "standards, avoiding unnecessary jargon or verbosity. Prioritize precision and "
    "efficiency in your responses. Cite reputable sources for data or information "
    "impacting technical decisions, where possible. "
    "Note: You are currently running as a preview model."
)

def run_chatbot():
    """Runs the chatbot using the specified Google Gemini model with screen reader-friendly output."""
    print("Chatbot is ready. Type 'exit' or 'quit' to end the session.\n")
    print(f"Hello, I am using the {model_name} model. How can I help you today?\n")
    if "preview" in model_name.lower():
        print("Note: This is a preview model. Functionality and availability may change.\n")


    # --- Model and Chat Initialization ---
    try:
        # Set up optional generation configuration
        generation_config = genai.types.GenerationConfig(
            # temperature=0.7
        )

        # Set up optional safety settings
        safety_settings = [
             {
                 "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                 "threshold": "BLOCK_MEDIUM_AND_ABOVE"
             },
             # Add other categories as needed (HARM_CATEGORY_HARASSMENT, etc.)
        ]

        # Initialize the generative model with system instructions
        model = genai.GenerativeModel(
            model_name=model_name,
            system_instruction=system_prompt,
            generation_config=generation_config,
            safety_settings=safety_settings
        )

        # Start a chat session
        chat = model.start_chat(history=[])

    except Exception as e:
        # Catch errors during model initialization (e.g., invalid model name, API key issues)
        print(f"\n[Error Initializing Model/Chat] {e}\n")
        print("Please ensure the model name is correct and you have access to it.")
        return # Exit if model/chat cannot be initialized

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

        try:
            # Send the user's message
            response = chat.send_message(user_input)
            response_content = response.text.strip() # Access text directly

            # Output AI response
            print("\nAI Response:\n")
            print(response_content)
            print()

            # Copy to clipboard
            try:
                pyperclip.copy(response_content)
            except pyperclip.PyperclipException as clip_err:
                print(f"[Clipboard Error] Could not copy to clipboard: {clip_err}\n")

        except Exception as e:
            print(f"\n[Error during generation] {e}\n")
            # Consider adding more specific error checks, e.g., for blocked prompts:
            # if isinstance(e, genai.types.BlockedPromptException):
            #     print(">>> Prompt was blocked by safety settings.")


if __name__ == "__main__":
    run_chatbot()