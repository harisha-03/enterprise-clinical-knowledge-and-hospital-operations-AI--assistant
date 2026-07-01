from app.rag.intent import IntentRouter


router = IntentRouter()

print("=" * 60)
print("Intent Router Test")
print("=" * 60)

while True:

    query = input("\nQuestion (exit to quit): ")

    if query.lower() == "exit":
        break

    intent = router.detect_intent(query)

    print(f"\nDetected Intent : {intent}")