from services.embedding_service import EmbeddingService


def main():

    print("=" * 60)
    print("TEST 3 : EMBEDDINGS")
    print("=" * 60)

    embedding = EmbeddingService().get_embedding_model()

    vector = embedding.embed_query("What is Phantom AV?")

    print(f"\nEmbedding Dimension : {len(vector)}")

    print("\nFirst 10 Values:\n")

    print(vector[:10])

    print("\nSUCCESS")


if __name__ == "__main__":
    main()