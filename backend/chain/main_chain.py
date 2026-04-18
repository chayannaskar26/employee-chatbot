from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

from models.openai_model import openai_llm
from retriever.hybrid_retrieve import hybrid_retrieve
from prompt.employee_prompt import employee_prompt
from prompt.rewrite_prompt import rewrite_prompt

parser = StrOutputParser()

retriever = RunnableLambda(hybrid_retrieve)

def get_context(retrieved_docs):
    return "\n\n".join(doc.page_content for doc in retrieved_docs)

def runChain(query: str):
    query_chain = rewrite_prompt | openai_llm | parser

    parallel_chain = RunnableParallel({
        'context': retriever | RunnableLambda(get_context),
        'question': RunnablePassthrough()
    })

    main_chain =  rewrite_prompt | openai_llm | parser | parallel_chain | employee_prompt | openai_llm | parser

    result = main_chain.invoke(query)

    return result
