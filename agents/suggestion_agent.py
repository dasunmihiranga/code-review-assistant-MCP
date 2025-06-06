from langchain.chains import LLMChain
from langchain_community.llms import Ollama
from langchain_groq import ChatGroq
import config
from prompts.suggestion_prompt import suggestion_prompt

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

def suggestion_agent(code_snippet: str) -> str:
    """
    Generate improvement suggestions for the code.
    
    Args:
        code_snippet: The code to analyze
        
    Returns:
        str: Improvement suggestions or error message
    """
    try:
        # Initialize LLM and chain
        llm = get_llm()
        chain = LLMChain(llm=llm, prompt=suggestion_prompt)
        
        # Run the chain
        result = chain.run(code_snippet=code_snippet)
        return result
    except Exception as e:
        return f"Error during suggestion generation: {str(e)}" 