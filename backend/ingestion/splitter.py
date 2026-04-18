from ingestion.loader import getDocuments
from langchain_text_splitters import RecursiveCharacterTextSplitter

def splitDocument():
    documents = getDocuments()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    doc_chunks = text_splitter.split_documents(documents)

    return doc_chunks