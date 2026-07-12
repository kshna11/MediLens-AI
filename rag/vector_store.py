from langchain_community.vectorstores import FAISS
from rag.embeddings import get_embeddings


def create_vector_store(chunks):
    """
    Create and save FAISS Vector Store
    """

    embeddings = get_embeddings()

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    vector_store.save_local("rag/faiss_index")

    return vector_store


def load_vector_store():
    """
    Load existing FAISS Vector Store
    """

    embeddings = get_embeddings()

    vector_store = FAISS.load_local(
        "rag/faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store