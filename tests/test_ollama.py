from services.ollama_service import OllamaService


def main():

    service = OllamaService()

    response = service.invoke("Say hello in one sentence.")

    print(response)


if __name__ == "__main__":
    main()
