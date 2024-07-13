import numpy as np
from sentence_transformers import SentenceTransformer


class VectorService:

    def create_vector(self, text: str):
        model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
        sentence_vectors = model.encode([text])
        vectors = np.array(sentence_vectors).tolist()
        return vectors[0]
