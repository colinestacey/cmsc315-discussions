# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

I simulated a DNS cache using Python dictionaries for this assignment. Using domain names as keys and their corresponding IPv4 addresses as values made it clear to me how beneficial hash tables are for real-life applications, especially if the data is accessed often. I had done some work with HashMap in Java and knew the basics of key value pairs but was not too familiar with the syntax of dictionaries in Python. I learned to appreciate the need to process missing keys correctly while going through the edge cases. A DNS cache missing a key doesn't necessarily mean there is a problem, it means the domain name has to be resolved before it can be added to the cache.

The major advantage of hash tables is that the average time complexity of searching is O(1), as opposed to O(n) for a linear search. But if there are two different keys that map to the same table index, a collision will occur. In Python, collisions are dealt with by using open addressing, which involves searching for open space in the hash table by employing a probing algorithm. The efficiency of hash tables makes them very useful in applications such as caching in DNS, where they are used for storing a large number of frequently accessed items without unnecessary overhead.