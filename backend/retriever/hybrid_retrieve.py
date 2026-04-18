from retriever.dense_retriever import dense_retriever
from retriever.sparse_retriever import bm25_retriever
from retriever.rerank import rerankDocs

def hybrid_retrieve(query):
    dense_docs = dense_retriever.invoke(query)
    sparse_docs = bm25_retriever.invoke(query)

    docs = dense_docs + sparse_docs
    unique_docs = {doc.page_content: doc for doc in docs}

    return rerankDocs(query, list(unique_docs.values()))