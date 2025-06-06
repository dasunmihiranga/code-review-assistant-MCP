# Code Review Assistant

## Project Description

The Code Review Assistant is a simple multi-agent system built using the Model Context Protocol (MCP) and LangChain. Its purpose is to provide automated, preliminary feedback on code snippets, including syntax checking, code explanation, and improvement suggestions. It can be integrated with MCP-compatible clients like Cursor IDE or Claude for Desktop.

## Features

- **Syntax Check:** Identifies potential syntax errors and structural issues.
- **Code Explanation:** Provides a high-level explanation of the code's functionality.
- **Suggestion Generation:** Offers actionable suggestions for code improvement.
- **MCP Server:** Exposes code review capabilities as a tool via the Model Context Protocol.
- **Flexible LLM Backend:** Supports both local Ollama models and the Groq API.

## File Structure

```
code_review_assistant/
├── .uv/                        # uv virtual environment directory (may be .venv based on your setup)
├── .env                        # Environment variables (sensitive config, ignored by git)
├── .gitignore                  # Specifies intentionally untracked files (.env, __pycache__, etc.)
├── code_review_server.py       # Main MCP server file (FastMCP instance, tool definitions)
├── agents/
│   ├── __init__.py             # Initializes the agents module
│   ├── syntax_check_agent.py   # Contains logic for SyntaxCheckAgent
│   ├── explanation_agent.py    # Contains logic for CodeExplanationAgent
│   └── suggestion_agent.py    # Contains logic for SuggestionAgent
├── prompts/
│   ├── syntax_check_prompt.py  # Prompt template for syntax checking
│   ├── explanation_prompt.py   # Prompt template for code explanation
│   └── suggestion_prompt.py    # Prompt template for suggestions
├── config.py                   # Non-sensitive, application-wide configurations
└── requirements.txt            # Project dependencies
```

## Setup

1.  **Clone the repository** (if applicable, or navigate to your project directory).

2.  **Install `uv`:** If you don't have `uv` installed, follow the official installation guide.
    ```bash
    # Example: via pipx
    pipx install uv
    ```

3.  **Navigate to the project directory:**
    ```bash
    cd your-project-directory # e.g., cd CRA-MCP/cra
    ```

4.  **Set up the virtual environment and install dependencies:**
    ```bash
    uv venv
    # Activate the virtual environment
    # On Windows:
    .venv\\Scripts\\activate
    # On macOS/Linux:
    source .venv/bin/activate
    
    # Install dependencies from requirements.txt
    uv sync
    ```

5.  **Configure Environment Variables:**
    Create a file named `.env` in the root of the project (same directory as `requirements.txt`). Copy the contents from `.sample.env` and fill in your actual configuration.
    
    ```env
    # Example .env content (copy from .sample.env)
    # ... your configuration here ...
    ```
    
    **Important:** Replace `<your_groq_api_key_here>` with your actual Groq API key if you plan to use Groq.
    
6.  **If using Ollama:**
    Download and install Ollama from [ollama.com](https://ollama.com/). Pull the required model (e.g., `qwen2.5-coder`) by running `ollama pull qwen2.5-coder` in your terminal. Ensure the Ollama server is running before starting the Code Review Assistant server.
    

## Running the Server

1.  **Activate the virtual environment** (if not already active):
    ```bash
    # On Windows:
    .venv\\Scripts\\activate
    # On macOS/Linux:
    source .venv/bin/activate
    ```
2.  **Run the server using `uv`:**
    ```bash
    uv run code_review_server.py
    ```
    The server will start and listen for connections from MCP clients.

## Using the Tool

Once the server is running, you can connect to it from an MCP-compatible client (like Cursor IDE chat or Claude for Desktop). The client should detect the available `code_review_assistant` server and expose the `review_code` tool.

Call the `review_code` tool with the code snippet you want to review:

```python
review_code("""
# Paste your code snippet here
def example_function(x):
    return x * 2
""")
```

The server will process the request using the configured LLM and return a consolidated code review including syntax feedback, explanation, and suggestions.

## Customization

- **Prompts:** Modify the prompt templates in the `prompts/` directory to adjust the behavior of each agent.
- **Agents:** Enhance the logic within the agent files (`agents/`) to include more complex processing or integrate with other tools/APIs.
- **Configuration:** Update `config.py` for application-wide settings or add new environment variables to `.env`.

---

**Note:** This is a starting point. Further development is needed to implement more sophisticated LLM interactions, error handling, and potentially integrate additional review aspects.
