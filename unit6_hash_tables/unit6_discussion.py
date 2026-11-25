"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # An empty dictionary is created and populated to simulate a DNS cache.
    # Each domain name is a unique key, and its corresponding IPv4 address is the value.
    #

    # Python's dictionaries behave like a hash table by using
    # a hash function to determine where key-value pairs are stored.
    dns_cache = {}
    dns_cache.update({
        "google.com": "74.125.136.113",
        "github.com": "140.82.114.3",
        "amazon.com": "98.87.170.71",
        "youtube.com": "108.177.122.190",
        "linkedin.com": "130.211.32.14"
    })
    print(dns_cache)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # .get() method returns the value associated with the specified key.
    # A hash function is used to efficiently locate the corresponding
    # value without the need for a linear search through every key.
    # This is what allows for an average time complexity of O(1).
    print("IP address for google.com:", dns_cache.get("google.com"))
    print("IP address for youtube.com:", dns_cache.get("youtube.com"))

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    # Assign a new IP address to an existing domain name
    # to simulate refreshing a DNS cache entry.
    # Because the key already exists, the previous value is replaced
    # rather than creating a duplicate entry, keeping the cache size the same.
    print("DNS cache before update:", dns_cache)
    dns_cache["google.com"] = "74.125.136.102"
    print("DNS cache after update:", dns_cache)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    # .pop() method removes the key-value pair from
    # the dictionary and returns the removed value.
    # Dictionary size is decreased by one.
    # This represents removing an expired DNS cache entry.
    print("DNS cache before deletion:", dns_cache)
    print("Key-value pair deleted: 'github.com':", dns_cache.pop("github.com"))
    print("DNS cache after deletion:", dns_cache)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1: Lookup a missing key (DNS cache miss)
    # Since the key github.com was deleted, the .get() method
    # returns None instead of raising a KeyError.
    print("Lookup missing key 'github.com':", dns_cache.get("github.com"))

    # Edge case 2: Update a missing key (Simulated DNS resolution and IP caching)
    # Assigning a value to a key that does not exist creates a new
    # key-value pair instead of updating an existing pair.
    # Dictionary size is increased by one.
    print("DNS cache before updating a missing key:", dns_cache)
    dns_cache["github.com"] = "140.82.114.35"
    print("DNS cache after updating a missing key:", dns_cache)

if __name__ == "__main__":
    main()