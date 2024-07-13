import os

from fastapi import Depends
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams


def get_qdrant_client() -> QdrantClient:
    qdrant_url = os.getenv("QDRANT_URL")
    return QdrantClient(url=qdrant_url)


class QdrantRepository:
    size: int = 384

    def __init__(
        self, qdrant_client: QdrantClient = Depends(get_qdrant_client)
    ) -> None:
        self.client = qdrant_client

    def create_collection(
        self,
        collection_name: str,
        distance: Distance = Distance.COSINE,
    ) -> None:
        self.client.recreate_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=self.size, distance=distance),
        )

    def store_qdrant(self, vectors: list, text: str):
        operation_info = self.client.upsert(
            collection_name="test_collection",
            wait=True,
            points=[
                PointStruct(id=1, vector=vectors, payload={"name": text}),
            ],
        )
        return operation_info
