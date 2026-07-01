from app.rag.chat import HospitalAIChat


chat = HospitalAIChat()

print("=" * 70)
print("Enterprise AI Hospital Assistant")
print("=" * 70)

while True:

    question = input("\nQuestion (exit to quit): ")

    if question.lower() == "exit":
        break

    result = chat.ask(question)

    print("\nIntent :", result["intent"])

    print("\nAnswer:\n")

   print(result["answer"])

   print("\nSources:\n")

    for source in result["sources"]:
         print(
            f"- {source['document']} (Page {source['page']})"
         )