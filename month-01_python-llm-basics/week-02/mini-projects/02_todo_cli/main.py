# To-Do List CLI (Beginner Version - Step 1)
# Stores tasks in memory only

tasks = []

while True:
    print("\nOptions: add, list, quit")
    choice = input("Enter choice: ").strip().lower()

    if choice == "add":
        task = input("Enter a task: ")
        tasks.append(task)
        print(f"✅ Added: {task}")

    elif choice == "list":
        if not tasks:
            print("📝 No tasks yet.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")

    elif choice == "quit":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice. Try again.")
