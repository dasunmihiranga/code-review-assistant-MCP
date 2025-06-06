from langchain.chains import LLMChain
from langchain_community.llms import Ollama
from langchain_groq import ChatGroq
import config
from prompts.explanation_prompt import explanation_prompt

def get_llm():
    """Initialize and return the appropriate LLM based on configuration."""
    if config.LLM_PROVIDER == "ollama":
        return Ollama(
            base_url=config.OLLAMA_BASE_URL,
            model=config.get_model_name()
        )
    elif config.LLM_PROVIDER == "groq":
        return ChatGroq(
            api_key=config.GROQ_API_KEY,
            model_name=config.get_model_name()
        )
    else:
        raise ValueError(f"Unsupported LLM provider: {config.LLM_PROVIDER}")

def explanation_agent(code_snippet: str) -> str:
    """
    Generate a clear explanation of the code's functionality.
    
    Args:
        code_snippet: The code to explain
        
    Returns:
        str: Code explanation or error message
    """
    try:
        # Initialize LLM and chain
        llm = get_llm()
        chain = LLMChain(llm=llm, prompt=explanation_prompt)
        
        # Run the chain
        result = chain.run(code_snippet=code_snippet)
        return result
    except Exception as e:
        return f"Error during code explanation: {str(e)}" 