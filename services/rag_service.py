import faiss
import numpy as np

from sentence_transformers import SentenceTransformer


class RAGService:

    def __init__(self):

        self.embedding_model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.index = None
        self.chunks = []

    def create_chunks(
        self,
        text,
        chunk_size=500,
        overlap=100
    ):

        text = text.strip()

        if not text:
            return []

        chunks = []

        start = 0

        while start < len(text):

            end = min(
                start + chunk_size,
                len(text)
            )

            chunks.append(
                text[start:end]
            )

            start += chunk_size - overlap

        return chunks

    def build_index(self, text):

        self.chunks = self.create_chunks(text)

        if not self.chunks:
            return

        embeddings = self.embedding_model.encode(
            self.chunks,
            convert_to_numpy=True
        )

        embeddings = embeddings.astype(
            np.float32
        )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(embeddings)

    def retrieve(
        self,
        query,
        top_k=3
    ):

        if self.index is None:
            return ""

        query_embedding = self.embedding_model.encode(
            [query],
            convert_to_numpy=True
        )

        query_embedding = query_embedding.astype(
            np.float32
        )

        _, indices = self.index.search(
            query_embedding,
            top_k
        )

        context = []

        for index in indices[0]:

            if 0 <= index < len(self.chunks):

                context.append(
                    self.chunks[index]
                )

        return "\n\n".join(context)

    def has_index(self):

        return self.index is not None

    def clear(self):

        self.index = None
        self.chunks = []