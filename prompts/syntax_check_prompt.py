from langchain.prompts import PromptTemplate

SYNTAX_CHECK_TEMPLATE = """
You are an expert code reviewer specializing in syntax analysis. Review the following code snippet and identify any syntax errors, missing brackets, unclosed strings, or basic structural issues.

Code to review:
{code_snippet}

Provide your analysis in the following format:
1. List any syntax errors found
2. List any structural issues (e.g., missing brackets, unclosed strings)
3. List any potential logical flow issues
4. If no issues are found, state "No syntax or structural issues found."

Your response should be clear and concise, focusing only on syntax and structural issues.
"""

syntax_check_prompt = PromptTemplate(
    input_variables=["code_snippet"],
    template=SYNTAX_CHECK_TEMPLATE
) 