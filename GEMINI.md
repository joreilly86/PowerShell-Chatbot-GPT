Of course. Based on your detailed requirements and the provided repository files, here is the Engineering Requirement Prompt (ERP) to execute this task.

-----

### **Engineering Requirement Prompt (ERP): Visually Impaired Professional's CLI Chatbot Enhancement**

This document outlines the development plan to enhance the existing PowerShell-Chatbot-GPT repository. The goal is to create a more flexible and robust suite of CLI tools for a visually impaired user, addressing current input limitations and expanding model availability.

-----

### **Pillar I: Curated Project Intelligence (The Context)**

This section defines the project's foundation by analyzing existing assets and requirements.

  * **Governing Documents & User Requirements:**

      * **Primary Objective:** Refactor the tool to accept multi-line text pasted from the clipboard, which is currently disrupted by line breaks.
      * **Model Expansion:** Integrate API support for five frontier models: **OpenAI, Google Gemini, Anthropic, Grok, and Perplexity.**
      * **Accessibility & Usability:**
          * Create five distinct and simply named `.bat` launcher files (e.g., `openai.bat`, `gemini.bat`) that handle environment activation and script execution.
          * Ensure the interface is compatible with Windows Dictation (Win + H) for voice-to-text input.
      * **User Persona Focus:** All modifications must maintain or improve accessibility for a visually impaired professional. The CLI interaction should be clear, and outputs must remain screen-reader friendly.

  * **Project-Specific Data (Analysis of Existing Repository):**

      * **Core Scripts (`bot.py`, `gem.py`, `plex.py`):** The repository uses two primary integration patterns:
        1.  **Direct SDK:** `gem.py` uses the `google-generativeai` library directly. This is the pattern for services with dedicated Python clients.
        2.  **OpenAI-Compatible Endpoint:** `plex.py` uses the `openai` library but points it to a third-party `base_url` (`https://api.perplexity.ai`). This is the pattern for services like Perplexity and Anthropic that offer OpenAI-compatible APIs. `bot.py` is a standard implementation using the `openai` library.
      * **Dependencies (`pyproject.toml`):** The project requires Python `>=3.12` and key libraries including `openai`, `google-generativeai`, `python-dotenv`, and `pyperclip`. New integrations must be compatible with this stack.
      * **Environment (`.env`):** The current architecture relies on API keys stored in a `.env` file (e.g., `OPENAI_API_KEY`, `GOOGLE_API_KEY`). This pattern will be extended.

  * **Precedent & Patterns:**

      * All new scripts must replicate the established structure: load environment variables, configure the client, define a system prompt, and contain the main `run_chatbot()` loop.
      * The user interaction flow—a clear "Hello" message, a "You:" prompt, and a formatted "AI Response:"—will be maintained across all scripts for a consistent user experience.

-----

### **Pillar II: Detailed Execution Strategy (The Implementation Blueprint)**

This section provides the step-by-step technical plan.

  * **Methodology:**

    1.  **Task 1: Resolve Multi-Line Input Handling**

          * **Action:** Modify the input mechanism in `bot.py`, `gem.py`, and `plex.py`.
          * **Implementation:** Replace the line-by-line `input()` function with a block-reading method. Import the `sys` library and use `sys.stdin.read()` to capture all text until an End-of-File (EOF) signal is received.
          * **User Instruction:** The CLI prompt must be updated to instruct the user to press **`Ctrl+Z` followed by `Enter`** on Windows to send the EOF signal after pasting their text.

        **Example Code Modification for `bot.py`:**

        ```python
        import os
        import sys  # <-- Add this import
        import pyperclip
        from dotenv import load_dotenv
        from openai import OpenAI

        # ... (client setup remains the same) ...

        def run_chatbot():
            # ... (initial prints remain the same) ...
            while True:
                try:
                    # --- MODIFIED INPUT BLOCK ---
                    print("You (Paste text, then press Ctrl+Z and Enter to send):")
                    user_input = sys.stdin.read().strip()
                    # --- END MODIFIED BLOCK ---
                except (EOFError, KeyboardInterrupt):
                    print("\nGoodbye!")
                    break
        # ... (rest of the loop remains the same) ...
        ```

    2.  **Task 2: Integrate Anthropic and Grok APIs**

          * **Action:** Create two new scripts: `anthropic.py` and `grok.py`.
          * **Implementation (`anthropic.py`):** Use the OpenAI-compatible endpoint pattern from `plex.py`. Initialize the `OpenAI` client with Anthropic's `api_key` and set the `base_url` to `https://api.anthropic.com/v1`.
          * **Implementation (`grok.py`):** Follow the same pattern. The `base_url` for Grok's API must be sourced from their official documentation (placeholder: `https://api.x.ai/v1`).
          * **Environment Variables:** Update the `.env` file (and a corresponding `.env.example`) to include keys for the new services:
            ```env
            ANTHROPIC_API_KEY=your_anthropic_api_key
            GROK_API_KEY=your_grok_api_key
            ```

    3.  **Task 3: Create `.bat` Launcher Files**

          * **Action:** In the root directory, create five batch files.
          * **Implementation:** Each file will contain commands to activate the virtual environment (assuming a `venv` folder as per the `.gitignore`), run the target Python script, and then deactivate.

        **`openai.bat`:**

        ```batch
        @echo off
        echo Starting OpenAI Chatbot...
        call venv\Scripts\activate.bat
        python bot.py
        deactivate
        pause
        ```

        *(Create four other `.bat` files—`gemini.bat`, `perplexity.bat`, `anthropic.bat`, `grok.bat`—by replacing `bot.py` with the corresponding script name.)*

    4.  **Task 4: Document Windows Dictation Workflow**

          * **Action:** Update the `README.md`.
          * **Implementation:** Add instructions explaining that Windows Dictation (**Win + H**) can be used to speak directly into the active CLI window. The user must activate it, dictate their query, and then press `Ctrl+Z` and `Enter` to submit the text to the model. No code changes are required for this feature.

  * **Deliverable Structure:**

      * Five modified/new Python scripts (`bot.py`, `gem.py`, `plex.py`, `anthropic.py`, `grok.py`), all implementing `sys.stdin.read()`.
      * Five `.bat` files for easy launching.
      * An updated `README.md` file with instructions for the new features.
      * An updated `.env.example` file listing all required API keys.

-----

### **Pillar III: Rigorous Validation Gates (The Verification Loop)**

This section defines the quality control process.

  * **Gate 1 (Compliance Check):**

      * All new and modified Python code must be linted, commented for clarity, and successfully run using Python 3.12, as specified in the project configuration.
      * All new dependencies must be added to `pyproject.toml` and locked.

  * **Gate 2 (Independent Verification):**

      * **Multi-Line Test:** For each of the five launchers, paste a multi-paragraph block of text from a PDF or text document. Verify that the entire block is processed as a single input and the LLM responds to the full context.
      * **Dictation Test:** For each launcher, use Windows Dictation to input a query. Verify that the dictated text is captured correctly and processed by the model.

  * **Gate 3 (Integration Review):**

      * Execute each `.bat` file and confirm the virtual environment is correctly activated and deactivated.
      * Confirm that the `pyperclip` functionality (copying the AI response to the clipboard) works for all five models.

  * **Gate 4 (Senior Review Package):**

      * Prepare a final commit with all new and modified files.
      * The `README.md` must be comprehensively updated to serve as the final user documentation. It should clearly explain:
        1.  How to add all five API keys to the `.env` file.
        2.  How to use the five new `.bat` launchers.
        3.  The new `Ctrl+Z` and `Enter` method for submitting pasted text.
        4.  The workflow for using Windows Dictation.