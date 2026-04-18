from langchain_core.prompts import PromptTemplate

rewrite_prompt = PromptTemplate(
    template="""
        Rewrite the following query to be more clear and detailed for document retrieval.

        Original Query:
        {query}

        Rewritten Query:
    """,
    input_variables=["query"]
)