from app.rag.memory import ConversationMemory


memory = ConversationMemory()

print("=" * 60)
print("Conversation Memory Test")
print("=" * 60)

while True:

    user = input("\nYou: ")

    if user.lower() == "exit":
        break

    memory.add_message("user", user)

    assistant = input("Assistant: ")

    memory.add_message(
        "assistant",
        assistant
    )

    print("\nCurrent Memory:\n")

    for msg in memory.get_history():

        print(msg)