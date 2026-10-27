# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.


This assignment was useful in helping me to understand how stacks and queues organize data as well as some applications of them. I learned how to use Python list to create a stack and collections.deque to create a queue. I also had some practice writing methods and handling potential exceptions.

A challenge I had was figuring out how to use the pop() method in my Stack class. At first, I was a little unsure about using the built-in .pop() method in a method I was making of the same name. However, Python's documentation popup helped me understand that the built-in method will remove the value and my method will decide how the stack will handle the removal operation.

Stacks are LIFO (Last In, First Out) structures, which are typically used in real-world applications for undoing recent actions in text editors, such as "undo last paragraph". First in, first out (FIFO) is helpful for managing print jobs or customer support tickets, as requests are processed in the order they are received.