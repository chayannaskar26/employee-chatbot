from langchain_community.vectorstores import FAISS

from ingestion.splitter import splitDocument
from models.openai_embedder import openai_embedder

def createVectorStore():
    doc_chunks = splitDocument()

    vector_store = FAISS.from_documents(doc_chunks, openai_embedder)

    return vector_store