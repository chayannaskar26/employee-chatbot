from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

from models.openai_model import openai_llm
from retriever.similarity_retriever import retriever
from prompt.prompt import employee_prompt

parser = StrOutputParser()

def get_context(retrieved_docs):
    return "\n\n".join(doc.page_content for doc in retrieved_docs)

def runChain(query: str):
    parallel_chain = RunnableParallel({
        'context': retriever | RunnableLambda(get_context),
        'question': RunnablePassthrough()
    })

    main_chain = parallel_chain | employee_prompt | openai_llm | parser

    result = main_chain.invoke(query)

    return result
