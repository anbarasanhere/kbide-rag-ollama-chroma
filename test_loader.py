from rag.loader import DocumentLoader

from rag.chunker import Chunker

loader = DocumentLoader("documents/kbide.docx")

documents = loader.load()

print("Documents loaded:", len(documents))

chunker = Chunker()

chunks = chunker.split(documents)

print("Chunks:", len(chunks))

print()

print(chunks[0].page_content[:500])