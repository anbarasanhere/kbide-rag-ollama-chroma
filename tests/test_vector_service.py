from services.vector_service import VectorService


def main():

    print("=" * 60)
    print("VECTOR SERVICE TEST")
    print("=" * 60)

    service = VectorService()

    db = service.get_vector_db()

    print()

    print(type(db))

    print()

    print("SUCCESS")


if __name__ == "__main__":
    main()
