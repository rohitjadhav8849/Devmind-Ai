from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)
import uuid


class QdrantVectorStore:

    def __init__(
        self,
        dimension
    ):

        self.client = QdrantClient(
            host="localhost",
            port=6333
        )

        self.collection_name = "documents"

        collections = self.client.get_collections()

        existing = [

            c.name

            for c in collections.collections

        ]

        if self.collection_name not in existing:

            self.client.create_collection(

                collection_name=self.collection_name,

                vectors_config=VectorParams(

                    size=dimension,

                    distance=Distance.COSINE

                )

            )
    
    def add(

        self,

        embedding,

        chunk,

        metadata

    ):

        point = PointStruct( # making of point

            id=str(uuid.uuid4()),

            vector=embedding.tolist(),

            payload={

                "text": chunk,

                **metadata

            }

        )

        self.client.upsert(

            collection_name=self.collection_name,

            points=[point]

        )

    def search(

        self,

        embedding,

        k=5

    ):

        hits = self.client.query_points(

        collection_name=self.collection_name,

        query=embedding.tolist(),

        limit=k

        ).points

        results = []

        for hit in hits:

            results.append({

                "chunk":

                hit.payload["text"],

                "score":

                hit.score,

               "metadata":

               hit.payload

            })

        return results