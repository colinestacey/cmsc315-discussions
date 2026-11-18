"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    # Worst case, a linear search has to sequentially check every element in the list.
    # This results in O(n) time complexity.
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """

    # Initialize the lower and upper bounds of the search range
    low = 0
    high = len(lst) - 1

    # Each iteration of the loop reduces the remaining search space by half.
    while high >= low:

        # Calculate the middle index of the current search range
        mid = (high + low) // 2

        # If the element found at the middle index is less than the target,
        # eliminate the left half of the search range and update the lower bound.
        if lst[mid] < target:
            low = mid + 1

        # If the element found at the middle index is greater than the target,
        # eliminate the right half of the search range and update the upper bound.
        elif lst[mid] > target:
            high = mid - 1

        # If neither condition is true, the target has been found.
        else:
            return mid
    return -1

def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")

    # Scores from one diver's six dives at a single competition.
    diver_scores = [42, 55, 61, 64, 68, 72]

    # Both search algorithms should find 68 at index 4, returning 4.
    print("Linear Search:", linear_search(diver_scores, 68))
    print("Binary Search:", binary_search(diver_scores, 68))

    # Both search algorithms should not find 80 and return -1.
    print("Linear Search (-1 expected):", linear_search(diver_scores, 80))
    print("Binary Search (-1 expected):", binary_search(diver_scores, 80))

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    # A linear search may need to check every score in the dataset,
    # while a binary search removes half of the remaining search space each iteration.
    # This makes a binary search more efficient as datasets grow larger.

    # Scores from all divers across multiple competitions.
    # The numerical values are placeholders for this example.
    all_scores = list(range(1, 10001))

    # Search for a score that exists near the end of the dataset.
    # Both search algorithms should find the target at index 9994.
    print("Linear Search:", linear_search(all_scores, 9995))
    print("Binary Search:", binary_search(all_scores, 9995))

    # Search for a score that does not exist.
    # Both search algorithms should return -1 because the target is not in the dataset.
    print("Linear Search (-1 expected):", linear_search(all_scores, 10005))
    print("Binary Search (-1 expected):", binary_search(all_scores, 10005))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Test searching an empty list of diving scores.
    empty_scores = []

    # Both algorithms should return -1 because no scores exist.
    print("Linear Search - Empty List (-1 expected):", linear_search(empty_scores, 68))
    print("Binary Search - Empty List (-1 expected):", binary_search(empty_scores, 68))

    # Test searching a list that contains only one score.
    single_score = [68]

    # Both algorithms should find 68 at index 0, returning 0.
    print("Linear Search - Single Item List:", linear_search(single_score, 68))
    print("Binary Search - Single Item List:", binary_search(single_score, 68))

if __name__ == "__main__":
    main()