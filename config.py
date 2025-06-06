# Configuration for the Code Review Assistant
# Loads sensitive values from environment variables using dotenv
import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# LLM configuration (use environment variables or fallback to defaults)
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "YOUR_GROQ_API_KEY")
LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME", "llama3")
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")  # e.g., "ollama" or "groq"

# Add any other non-sensitive, application-wide config below 