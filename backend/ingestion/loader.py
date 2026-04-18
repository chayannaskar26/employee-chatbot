import os
from langchain_community.document_loaders import PyPDFLoader

def getDocuments():

    documents = []

    for file in os.listdir('./documents/'):
        if file.endswith(".pdf"):
            pdf_path = os.path.join('./Documents/', file)
            loader = PyPDFLoader(pdf_path)
            docs = loader.load()
            documents.extend(docs)

    return documents

