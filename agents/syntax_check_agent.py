from langchain.chains import LLMChain
from langchain_community.llms import Ollama
from langchain_groq import ChatGroq
import config
from prompts.syntax_check_prompt import syntax_check_prompt

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

def syntax_check_agent(code_snippet: str) -> str:
    """
    Analyze code for syntax errors and structural issues.
    
    Args:
        code_snippet: The code to analyze
        
    Returns:
        str: Analysis results or error message
    """
    try:
        # Initialize LLM and chain
        llm = get_llm()
        chain = LLMChain(llm=llm, prompt=syntax_check_prompt)
        
        # Run the chain
        result = chain.run(code_snippet=code_snippet)
        return result
    except Exception as e:
        return f"Error during syntax check: {str(e)}" 