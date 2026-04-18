from langchain_core.prompts import PromptTemplate

employee_prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided documents context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)