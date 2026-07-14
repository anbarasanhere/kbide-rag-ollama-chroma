import subprocess
import sys

tests = [

    "tests.test_context",

    "tests.test_logger",

    "tests.test_loader",

    "tests.test_chunker",

    "tests.test_embedding_service",

    "tests.test_vector_service",

    "tests.test_retriever",

    "tests.test_similarity",

    "tests.test_prompt",

    "tests.test_ollama"

]

print("=" * 70)
print("KBIDE AI - BASELINE TEST SUITE")
print("=" * 70)

for test in tests:

    print(f"\nRunning {test}")

    result = subprocess.run(
        [sys.executable, "-m", test]
    )

    if result.returncode != 0:

        print(f"\nFAILED : {test}")

        break

print("\nAll baseline tests completed.")
