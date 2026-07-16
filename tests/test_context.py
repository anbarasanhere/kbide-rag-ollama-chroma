from core.app_context import context


def main():

    print("=" * 60)
    print("APP CONTEXT TEST")
    print("=" * 60)

    print()

    print("Context created")

    print()

    print("No services loaded yet.")

    print()

    print("Current cache:")

    print(context._services)

    print()

    input("Press ENTER to load LLM...")

    _ = context.llm

    print()

    print(context._services)

    print()

    input("Press ENTER to load Embedding...")

    _ = context.embedding

    print()

    print(context._services)

    print()

    print("SUCCESS")


if __name__ == "__main__":
    main()
