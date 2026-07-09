from typing import List


class TextChunker:

    def __init__(self,
                 chunk_size: int = 100, # size of chunk
                 chunk_overlap: int = 5): # overlapping characters size
        # by default 500,100cd
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk(self, text: str) -> List[str]:

        chunks = []

        start = 0

        while start < len(text):

            end = start + self.chunk_size

            chunk = text[start:end]

            chunks.append(chunk)

            start += self.chunk_size - self.chunk_overlap

        return chunks