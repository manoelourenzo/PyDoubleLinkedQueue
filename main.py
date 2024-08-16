from LinkedQueue import *



queue = Queue()

while True:
        queue.showQueue()
        print("\nCircular Queue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Show Queue")
        print("4. Clear Queue")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            item = input("Enter the item to enqueue: ")
            queue.enqueue(item)
            print(f"{item} enqueued into the Circular Queue.")

        elif choice == "2":
            if not queue.isEmpty():
                removed_item = queue.dequeue()
                print(f"{removed_item} dequeued from the Circular Queue.")
            else:
                print("Circular Queue is empty. Cannot dequeue.")

        elif choice == "3":
            queue.showQueue()

        elif choice == "4":
            queue.clear()
            print("Circular Queue cleared.")

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option (1-5).")

if __name__ == "__main__":
    main()
