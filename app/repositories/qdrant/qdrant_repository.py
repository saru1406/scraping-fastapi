import os

from fastapi import Depends
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams


def get_qdrant_client() -> QdrantClient:
    qdrant_url = os.getenv("QDRANT_URL")
    return QdrantClient(url=qdrant_url)


class QdrantRepository:

    def __init__(
        self, qdrant_client: QdrantClient = Depends(get_qdrant_client)
    ) -> None:
        self.client = qdrant_client

    def create_collection(
        self,
        collection_name: str,
        vector_size: int,
        distance: Distance = Distance.COSINE,
    ) -> None:
        self.client.recreate_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=vector_size, distance=distance),
        )
