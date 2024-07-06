from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db

from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

router = APIRouter()

@router.post("/prompt", tags=['prompt'])
def prompt():
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    sentences = ["私は山田太郎です。", "私は田中花子です。", "これはテスト文章です。"]
    sentence_vectors = model.encode(sentences)
    # ベクトルの次元数を取得
    d = sentence_vectors.shape[1]

    # Faissインデックスを作成
    index = faiss.IndexFlatL2(d)
    index.add(sentence_vectors)
    faiss.write_index(index, "faiss_index_ivf.bin")
    print(d)
