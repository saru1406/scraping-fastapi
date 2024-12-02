import numpy as np
from sentence_transformers import SentenceTransformer


class VectorService:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
    
    def create_vector(self, text: str):
        sentence_vectors = self.model.encode([text])
        return sentence_vectors[0].tolist()
