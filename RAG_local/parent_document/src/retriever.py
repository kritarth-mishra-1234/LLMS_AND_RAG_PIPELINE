from typing import List
from .document_loader import Document
from .text_splitter import TextSplitter
from .vector_store import VectorStore

class Retriever:
    def __init__(
        self,
        vector_store: VectorStore,
        parent_splitter: TextSplitter,
        child_splitter: TextSplitter
    ):
        self.vector_store = vector_store
        self.parent_splitter = parent_splitter
        self.child_splitter = child_splitter

    def add_documents(self, documents: List[Document]):
        # Split into parent documents
        parent_docs = self.parent_splitter.split_documents(documents)
        
        # Split parents into children
        for parent_doc in parent_docs:
            child_docs = self.child_splitter.split_documents([parent_doc])
            self.vector_store.add_documents(child_docs)

    def get_relevant_documents(self, query: str, k: int = 4) -> List[Document]:
        return self.vector_store.similarity_search(query, k)