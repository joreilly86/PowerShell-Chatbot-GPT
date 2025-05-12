# Chatbot for Visually Impaired Professionals 🚀

## Project Overview 📖

This chatbot is a simple yet powerful tool designed to assist visually impaired professionals, with a focus on civil engineering in this example. However, its versatile nature allows it to be easily adapted for various fields. It leverages OpenAI's GPT-4 Turbo model to generate accurate and context-aware responses. A standout feature of this chatbot is its ability to automatically copy responses to the clipboard, enhancing usability for visually impaired users. For more resources and tools for engineers interested in Python, visit [flocode.dev](https://flocode.dev).

## How It Works 🧠

- **Language Model**: Utilizes OpenAI's GPT-4 Turbo for comprehensive language understanding and response generation. This model excels in providing detailed answers tailored to a wide array of professional queries.

- **Accessibility Focused**: Designed for visually impaired users, with responses automatically copied to the clipboard for ease of use.

- **Adaptable Conversations**: Maintains conversational context, ideal for a series of interconnected queries and responses.

- **User-Friendly Interface**: Operates via a command-line interface, ensuring simplicity in interaction. Just type your question and receive an instant response.

## Setup and Usage 🛠️

1. **Prerequisites**:
   - Python installation.
   - Install required packages using the following command:
     ```bash
     pip install -r requirements.txt
     ```

2. **Environment Variables**:
   - Create a `.env` file in the root directory of the project.
   - Add your OpenAI API key to the file:
     ```env
     OPENAI_API_KEY=your_openai_api_key
     ```

3. **Running the Chatbot**:
   - Launch the script in a CLI using:
     ```bash
     python chatbot.py
     ```
   - Input your queries, and the chatbot will respond accordingly.
   - Responses are automatically copied to your clipboard for immediate pasting.

4. **Exiting**:
   - Type 'exit' or 'quit' to close the chatbot.

## Limitations and Notes ⚠️

- **Accuracy Check**: Always verify technical advice manually.
- **API Key Security**: Keep your OpenAI API key confidential and do not share it publicly.
- **Internet Dependency**: Requires an active internet connection.
- **Clipboard Functionality**: Ensure `pyperclip` is installed and supported on your system for clipboard copying.

## Supported Models 🤖

- **GPT-4o**: OpenAI's flagship model, known for its comprehensive language understanding and response generation.
- **Gemini**: Google's cutting-edge model, offering advanced capabilities in various tasks.
- **Perplexity**: A powerful model focused on providing accurate and concise answers to complex questions.

## Conclusion 🎉

This chatbot serves as a resource for visually impaired professionals, streamlining information access and fostering independent, efficient working methods. While this example is tailored for civil engineering, the model can be easily customized for various professional needs.
