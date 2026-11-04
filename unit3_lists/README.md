# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

I thought a navigation bar in a web page provided a convenient example for list operations because all the links have a location. Menu labels were stored in one list and each function was used to add, remove, and search for links. The test cases show how a list changes as pages are added or removed.

The assignment helped reinforce the concepts of element shifting and index validation for me. After several operations on the same list, it became harder to keep track of positions. I found that using len(menu) to get middle and end indexes instead of the positions was a good way to stop using the outdated positions.

The performance of an operation is dependent on its location. An array-based list has O(n) time for inserting and deleting elements at the beginning. Having to check all elements to find a particular element in an unsorted list will take O(n), while accessing it by index will have a time complexity of O(1). These differences become more significant the larger the lists.

A linked list can be optimized for the frequent insertion and deletion of nodes when the necessary node references are provided already without shifting of the surrounding elements. But traversal is needed for finding a position, so an array-based list would be useful for direct indexing.
