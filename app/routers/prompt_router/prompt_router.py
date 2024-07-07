import faiss
import numpy as np
from fastapi import APIRouter, Depends, HTTPException
from sentence_transformers import SentenceTransformer
from sqlalchemy.orm import Session
from app.repositories.qdrant.qdrant_repository import QdrantRepository

from app.database import get_db

router = APIRouter()


@router.post("/prompt", tags=["prompt"])
def prompt(qdrant_repository: QdrantRepository = Depends(QdrantRepository)):
    model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
    sentences = ["私は山田太郎です。", "私は田中花子です。", "これはテスト文章です。"]
    sentence_vectors = model.encode(sentences)
    # ベクトルの次元数を取得
    vector_size = sentence_vectors.shape[1]

    # Faissインデックスを作成
    # index = faiss.IndexFlatL2(vector_size)
    # index.add(sentence_vectors)
    # faiss.write_index(index, "faiss_index_ivf.bin")

    qdrant_repository.create_collection('test', vector_size)
