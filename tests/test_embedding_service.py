from services.embedding_service import EmbeddingService

def main():

    embedding = EmbeddingService().get_embedding_model()

    vector = embedding.embed_query("What is KBIDE?")

    print(f"Embedding Length : {len(vector)}")

    print(vector[:5])


if __name__ == "__main__":
    main()
