from vector_store.vector_store import createVectorStore

store = createVectorStore()
dense_retriever = store.as_retriever(search_type="similarity", search_kwargs={"k": 4})