# PowerShell-AI-Chatbot: A User-Friendly AI Chat Suite

## 1. Introduction for the User

Welcome! This is a collection of simple, powerful chatbots designed to be easy to use. Think of it as having several expert assistants ready to answer your questions directly from your computer.

This project is designed for vision impaired users and features a simpified command line UI, streamlined to allow for real work.

For more engineering tools, check out the [**Flocode Newsletter**](https://flocode.substack.com/). 

James 🌊

**What Can It Do?**
-   **Answer Questions:** Ask anything from simple questions to complex technical queries.
-   **Analyze Text:** Paste long documents, articles, or emails and ask for summaries, analysis, or key takeaways.
-   **Automatic Copying:** Every answer the AI gives is automatically copied to your clipboard, making it easy to paste into other applications.
-   **Voice and Paste Friendly:** Designed to work smoothly with Windows Dictation and for pasting text from other sources.

You have access to five different AI "brains" (models):
-   **OpenAI** (the makers of ChatGPT)
-   **Gemini** (from Google)
-   **Anthropic** (makers of Claude)
-   **Perplexity**
-   **Grok**

Each has its own launcher file, so you can choose the best assistant for your task.

---

## 2. Guide for Daily Use

This section explains how to use the chatbots day-to-day.

### How to Start a Chatbot
On your computer, you will find five special launcher files called "batch files." They end in `.bat`. Think of them as shortcuts to start each AI assistant.

-   `openai.bat`
-   `gemini.bat`
-   `perplexity.bat`
-   `anthropic.bat`
-   `grok.bat`

To start a chat, simply **double-click** on the file for the AI you want to use. A new terminal window will open, and the chatbot will be ready.

### How to Ask a Question (Two Methods)
You have two ways to ask a question: a simple one for quick chats, and a special one for pasting long text.

**Method 1: Simple Chat (For single lines)**

1.  When the chatbot is ready, it will show: `You:`
2.  Simply type your question and press **`Enter`**.

This is best for quick questions or commands.

**Method 2: Paste Mode (For multi-line text from PDFs, emails, etc.)**

Use this method when you need to paste a block of text that has multiple lines or paragraphs.

1.  At the prompt, type the word `PASTE` and press **`Enter`**.
2.  The chatbot will confirm you are in paste mode and will say:
    `(Multi-line mode: Paste your text now, then type 'ENDPASTE' on a new line and press Enter)`
3.  You can now paste your entire block of text. Don't worry about line breaks or blank lines.
4.  When you are finished, type the word `ENDPASTE` on a new, empty line and press **`Enter`**.

This tells the chatbot, "Okay, I'm done. It's your turn to answer."

### Using Voice to Text (Windows Dictation)
You can talk to the chatbot instead of typing.

1.  When it's your turn to ask a question, press and hold the **`Windows`** key and then press the **`H`** key. This opens the Windows Dictation toolbar.
2.  Start speaking. Your words will appear in the terminal.
3.  When you are finished talking, press **`Enter`** to send your message. If you dictated a long message, you may need to use the `PASTE` mode.

### What Happens Next?
-   After you send your message, the chatbot will say: `AI is thinking...`
-   It will then write its response in the window.
-   The **entire response is automatically copied to your clipboard**. You can immediately paste it into an email, document, or any other application.

### How to End a Chat Session
When you are finished with your chat, you can simply type `exit` or `quit` and press **`Enter`**. The window will close.

---

## 3. First-Time Setup Guide

This section explains how to install the project on a new computer.

### Step A: Prerequisites
The following software must be installed on the system first.
1.  **Git:** A version control tool needed to copy the project files. [Download Git here](https://git-scm.com/downloads).
2.  **Python 3.12+:** The programming language the chatbots are written in. [Download Python here](https://www.python.org/downloads/). During installation, ensure you check the box that says **"Add Python to PATH"**.
3.  **uv:** A fast, modern Python package installer. Instructions for installing `uv` can be found [here](https://github.com/astral-sh/uv).

### Step B: Installation
1.  **Clone the repository:** Open a Command Prompt or PowerShell and run:
    ```bash
    git clone <your-github-repository-url>
    cd PowerShell-Chatbot-GPT
    ```
2.  **Install dependencies:** This command reads the `pyproject.toml` file and creates a virtual environment with everything needed.
    ```bash
    uv sync
    ```

### Step C: API Key Configuration
The chatbots need special passwords, called API keys, to work.

1.  **Explain API Keys to the User:** Let the user know that API keys are like passwords for a program and must be kept private. They will need to sign up for accounts on the respective AI provider websites (OpenAI, Google AI, Anthropic, etc.) to get their own keys.

2.  **Create the `.env` file:** In the project folder, make a copy of the example file.
    ```bash
    copy .env.example .env
    ```

3.  **Add the Keys:** Open the new `.env` file in a text editor (like Notepad). Paste the user's API keys after the `=` sign for each service. The file includes all the keys needed.
    ```env
    # Example:
    OPENAI_API_KEY=paste_the_openai_key_here
    GOOGLE_API_KEY=paste_the_google_key_here
    # ...and so on for the others.
    ```
    Save and close the file. The project is now ready to use.

---

## 4. Troubleshooting

-   **Window closes immediately after starting:** This usually means an API key is missing or incorrect in the `.env` file. Double-check that the correct key has been pasted.
-   **"Module not found" error:** This means the dependencies were not installed correctly. Re-run the installation steps (Step B).
-   **`pyperclip` errors:** If you see an error about the clipboard, it may indicate an issue with the `pyperclip` library on the system, but this is uncommon on Windows.
