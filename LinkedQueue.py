class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, item):
        """
        Adds an element to the rear of the queue.

        Args:
            item: Element to be added to the queue.
        """
        newNode = Node(item)
        if self.isEmpty():
            # If the queue is empty, set both front and rear to the new node
            self.front = newNode
            self.rear = newNode
        else:
            # If the queue is not empty, update the rear and link the new node
            newNode.prev = self.rear
            self.rear.next = newNode
            self.rear = newNode

        self.size += 1

    def dequeue(self):
        """
        Removes and returns the element from the front of the queue.

        Returns:
            item: Element removed from the front of the queue.
        """
        if not self.isEmpty():
            removed_item = self.front.item
            self.front = self.front.next

            # If the queue becomes empty after dequeue, update rear to None
            if self.front is None:
                self.rear = None

            self.size -= 1
            return removed_item
        else:
            # Return None or raise an exception to handle dequeue from an empty queue
            return None  # or raise IndexError("Cannot dequeue from an empty queue")

    def showQueue(self):
        """
        Displays the elements in the circular queue.
        """
        if self.isEmpty():
            print("Queue is empty.")
        else:
            print("Circular Queue Elements:")
            currentNode = self.front
            while currentNode:
                print("|", currentNode.item, "|", end=" ")
                currentNode = currentNode.next
            print("\n")

    def clear(self):
        self.front = None
        self.rear = None
        self.size = 0