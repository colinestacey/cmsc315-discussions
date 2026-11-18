# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.


This task helped me to gain a better understanding of linear search and binary search, and how the one can be more efficient than the other. A linear search examines elements one by one until it reaches the desired element; a binary search, instead, discards half of the remaining search space using the middle element. This helped me understand the difference between their time complexities, O(n) and O(log n).

A problem I had was with some of the minor details while coding a binary search. I had to be careful to work out the middle index properly and use integer division (//) rather than decimal division (/). Working through the code and understanding why those details mattered helped me get more comfortable implementing the algorithms.

In my real-life example, a diving score/competition database, linear search would serve as an appropriate method to search through a short list of scores of a single diver on a single competition. If multiple divers and competitions produced thousands of scores, however, and the database had to examine them all, binary search would be more efficient, provided that the data is sorted. The primary disadvantage is that binary search does not work with unsorted data, whereas linear search does.