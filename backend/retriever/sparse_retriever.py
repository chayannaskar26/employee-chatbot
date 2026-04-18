from langchain_community.retrievers import BM25Retriever
from ingestion.splitter import splitDocument

split_docs = splitDocument()
bm25_retriever = BM25Retriever.from_documents(split_docs)
bm25_retriever.k = 4