import pandas as pd
from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_CODES = BASE_DIR / "Model_codes"

BOOKS_PATH = MODEL_CODES / "books_with_emotions.csv"

DESCRIPTION_PATH = MODEL_CODES / "tagged_description.txt"

VECTOR_DB_PATH = BASE_DIR / "vector_db"


class SemanticBookRetriever:

    def __init__(
        self,
        books_path=BOOKS_PATH,
        descriptions_path=DESCRIPTION_PATH,
        embedding_model="BAAI/bge-small-en"
    ):

        # Load books dataset
        self.books = pd.read_csv(books_path)

        # Load tagged descriptions
        raw_documents = TextLoader(
            descriptions_path,
            encoding="utf-8"
        ).load()

        # Split documents
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=0
        )

        self.documents = text_splitter.split_documents(
            raw_documents
        )

        # Load embedding model
        self.embedding_model = HuggingFaceEmbeddings(
            model_name=embedding_model
        )

        # Create vector database
        if VECTOR_DB_PATH.exists():

            self.db_books = Chroma(
                persist_directory=str(VECTOR_DB_PATH),
                embedding_function=self.embedding_model
            )

        else:

            self.db_books = Chroma.from_documents(
                documents=self.documents,
                embedding=self.embedding_model,
                persist_directory=str(VECTOR_DB_PATH)
            )

    def retrieve_semantic_books_recommendation(
        self,
        user_query,
        k=10
    ):

        # Semantic retrieval
        recommended = self.db_books.similarity_search(
            query=user_query,
            k=k
        )

        # Extract ISBN values
        isbn_list = []

        for doc in recommended:

            try:
                isbn = int(
                    doc.page_content
                    .strip('"')
                    .split()[0]
                )

                isbn_list.append(isbn)

            except:
                continue

        # Retrieve books preserving order
        retrieved_books = (
            self.books
            .set_index("isbn13")
            .loc[isbn_list]
            .reset_index()
        )

        return retrieved_books

