"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""
import collections
from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []


    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Appends the next item to the end of the list so that they may be
        # removed first, which supports LIFO behavior
        self.items.append(value)


    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Check if the stack is empty before removing and returning the last item
        # .pop() removes the last item in a list, following LIFO behavior
        if len(self.items) == 0:
            return "Stack is empty."
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # After checking if the stack is empty, peek returns what is on top
        # of the stack without removing it or changing the order of the list
        if len(self.items) == 0:
            return "Stack is empty."
        item = self.items[-1]
        return item


    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        if len(self.items) == 0:
            return True
        return False


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = collections.deque()


    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Appends the next item to the end of the queue, allowing the front item
        # to be removed first, which supports FIFO behavior
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Checking if the queue is empty prevents the method from raising
        # an exception when popleft() is called
        if len(self.items) == 0:
            return "Queue is empty."
        return self.items.popleft()


    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Returning the item at index 0 will return the front value without
        # removing it or changing the order of the queue
        if len(self.items) == 0:
            return "Queue is empty."
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        if len(self.items) == 0:
            return True
        return False


def main():
    print("\n=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


    print("\n=== STACK DEMO ===")
    print("TODO: Create a Stack object, demonstrate LIFO behavior.")

    stack1 = Stack()
    stack2 = Stack()
    emptyStack = Stack()

    stack1.push(10)
    stack1.push(20)
    stack1.push(30)
    stack1.push(40)

    stack2.push(10)

    print("\nPushed 4 values to stack1.")
    print("First value popped from stack1:", stack1.pop())
    print("Second value popped from stack1:", stack1.pop())
    print("Using pop() when the stack is empty returns:", emptyStack.pop())
    print("Using peek() when the stack is empty returns:", emptyStack.peek())
    print("Removed the only value from stack2:", stack2.pop())
    print("Check that stack2 is empty:", stack2.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")
    print("TODO: Create a Queue object, demonstrate FIFO behavior.")

    queue1 = Queue()
    queue2 = Queue()
    emptyQueue = Queue()

    queue1.enqueue(10)
    queue1.enqueue(20)
    queue1.enqueue(30)
    queue1.enqueue(40)

    queue2.enqueue(10)

    print("\nAdded 4 values to queue1.")
    print("First value dequeued from queue1:", queue1.dequeue())
    print("Second value dequeued from queue1:", queue1.dequeue())
    print("Using dequeue() when the queue is empty returns:", emptyQueue.dequeue())
    print("Using front() when the queue is empty returns:", emptyQueue.front())
    print("Removed the only value from queue2:", queue2.dequeue())
    print("Check that queue2 is empty:", queue2.is_empty())


if __name__ == "__main__":
    main()
