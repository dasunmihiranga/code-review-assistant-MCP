# Configuration for the Code Review Assistant
# Loads sensitive values from environment variables using dotenv
import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# LLM Configuration
# Ollama settings
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL_NAME = os.getenv("OLLAMA_MODEL_NAME", "qwen2.5-coder")

# Groq settings
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "YOUR_GROQ_API_KEY")
GROQ_MODEL_NAME = os.getenv("GROQ_MODEL_NAME", "llama3-70b-8192")

# Default LLM provider (can be "ollama" or "groq")
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")

# Model names based on provider
def get_model_name():
    """Get the appropriate model name based on the selected provider."""
    if LLM_PROVIDER == "ollama":
        return OLLAMA_MODEL_NAME
    elif LLM_PROVIDER == "groq":
        return GROQ_MODEL_NAME
    else:
        raise ValueError(f"Unsupported LLM provider: {LLM_PROVIDER}")

# Add any other non-sensitive, application-wide config below 