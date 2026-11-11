# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

This week I implemented a binary search tree to store VLAN IDs of a network. I learned how to perform an in-order traversal then added and searched IDs recursively. I did also attempt to add a duplicate and test the results. One VLAN 30 remained in my program, because the insertion helper skips over equal values.

One difficulty was grasping why the insertion helper returns a node. I was able to get through it by looking at how VLAN 20 was inserted. The root value of 40 is greater than 20 so the helper is called on the left child. The node is not occupied, so a new node is created, and returned by the recursive call. That value is assigned to the node's left link, thus attaching VLAN 20 to the tree.

With the same ordering, searching is more efficient. The program can skip over the entire left subtree of 40 as all the values in it are smaller than 40. When the list is not sorted a linear search can be used which might require every list item to be checked. If the BST is balanced the worst case time complexity is O(log n) and if the BST is skewed the worst case time complexity is O(n).