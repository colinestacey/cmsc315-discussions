"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Existing elements at and after the insertion index shift right.
    Inserting at the beginning shifts all elements for an O(n) time complexity.
    Inserting at the end is usually O(1) time complexity, unless resizing occurs.
    """
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Check for a valid index to prevent an IndexError. If index is invalid, return None without changing the list.
    Remove the element at the specified index and return it.
    Elements after the removed item shift left to fill the empty space.
    """
    if (index < 0) or (index >= len(lst)):
        return None
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Return the first index of value in the list, or -1 if no such value.
    This for loop is a linear search because it visits elements of a list one at a time.
    The list may be unsorted, so the search checks each element in the list sequentially.
    """
    for index, item in enumerate(lst):
        if item == value:
            return index
    return -1

def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    # Create and display the website's original navigation menu for all tests
    menu = ["Home", "About", "Services", "Contact", "Login", "FAQ"]
    print("Original list:", menu)

    print("\n=== INSERTION TESTS ===")

    # Insert element "Dashboard" at the beginning, all existing elements shift right.
    insert_at(menu, 0, "Dashboard")
    print("List after insertion at the beginning:", menu)

    # Insert element "Resources" at the current middle index, elements at and after it shift right
    insert_at(menu, len(menu) // 2, "Resources")
    print("List after insertion in the middle:", menu)

    # Insert element "Support" at the end, no shifts are required.
    insert_at(menu, len(menu), "Support")
    print("List after insertion at the end:", menu)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Remove the first element "Dashboard" in the list, all remaining items shift left.
    print("Element removed:", delete_at(menu, 0))
    print("List after deletion at the beginning:", menu)

    # Remove the element "Contact" located at the current middle index
    print("Element removed:", delete_at(menu, len(menu) // 2))
    print("List after deletion in the middle:", menu)

    # Remove the element "Support" from the last valid index of the current menu
    print("Element removed:", delete_at(menu, len(menu) - 1))
    print("List after deletion at the end:", menu)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # Search for element "Resources" in the list, which exists at index 2.
    print("Index of 'Resources':", search_value(menu, "Resources"))

    # Search for element "Search" in the list, which does not exist. The search returns -1.
    print("Index of 'Search':", search_value(menu, "Search"))

    # Display the list to confirm the search did not change it.
    print("List after search:", menu)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Attempt to delete an element using an invalid index, return None without changing the list
    print("Delete an element at an invalid index:", delete_at(menu, len(menu)))
    print("List after an invalid deletion:", menu)

    # Insert the element "Home" into an empty list.
    empty_menu = []
    print("\nOriginal empty list:", empty_menu)
    insert_at(empty_menu, 0, "Home")
    print("List after inserting an element into an empty list:", empty_menu)

if __name__ == "__main__":
    main()