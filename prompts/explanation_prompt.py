from langchain.prompts import PromptTemplate

EXPLANATION_TEMPLATE = """
You are an expert code reviewer specializing in code explanation. Analyze the following code snippet and provide a clear, concise explanation of its functionality.

Code to explain:
{code_snippet}

Provide your explanation in the following format:
1. Main Purpose: What is the primary purpose of this code?
2. Key Components: What are the main components or functions?
3. Data Flow: How does data flow through the code?
4. Important Details: Any notable implementation details or patterns used?

Keep your explanation clear and concise, focusing on the high-level understanding of the code's functionality.
"""

explanation_prompt = PromptTemplate(
    input_variables=["code_snippet"],
    template=EXPLANATION_TEMPLATE
) 