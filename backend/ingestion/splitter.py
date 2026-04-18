from ingestion.loader import getDocuments
from langchain_text_splitters import CharacterTextSplitter

def splitDocument():
    documents = getDocuments()

    text_splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    doc_chunks = text_splitter.split_documents(documents)

    return doc_chunks