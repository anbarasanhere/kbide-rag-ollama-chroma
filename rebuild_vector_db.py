"""
Rebuild the Vector Database
"""
from services.vector_service import VectorService


def main():

    print("=" * 50)
    print("REBUILDING VECTOR DATABASE")
    print("=" * 50)

    vector_service = VectorService()

    vector_service.rebuild()

    db = vector_service.get_vector_db()

    print(f"\nDocuments Indexed: {db._collection.count()}")

    print("\nVector database rebuilt successfully.")


if __name__ == "__main__":
    main()
