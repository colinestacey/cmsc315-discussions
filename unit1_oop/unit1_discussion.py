"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""

import copy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    device_type = "Computer"

    def __init__(self, device_name, status):
        self.device_name = device_name
        self.status = status

    def display_info(self):
        print(f"Device name: {self.device_name}, Status: {self.status}")


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    server_role = "Storage"

    def __init__(self, device_name, status, capacity, location):
        super().__init__(device_name, status)
        self.capacity = capacity
        self.location = location

    def get_capacity(self):
        return self.capacity

    def display_info(self):
        print(f"Server name: {self.device_name}, Status: {self.status}, Capacity: {self.capacity}, Location: {self.location}")

    # Student-created extension
    def update_status(self, status):
        self.status = status


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    print("TODO: Implement namespace demonstration")
    server1 = ChildClass("Server1", "Online", 500, "Office A")
    server2 = ChildClass("Server2", "Offline", 1000, "Office B")

    print(ChildClass.server_role)
    print(server1.server_role)

    server1.ip_address = "192.168.1.20"

    print(server1.__dict__)
    print(server2.__dict__)

    print(ChildClass.__dict__)

# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    print("TODO: Implement shallow copy and deep copy demonstration")

    server = {"name": "Server1", "storage": [500, 1000]}

    # Shallow copy creates a new dictionary but references the same nested list
    shallow = copy.copy(server)

    # Deep copy creates a new dictionary a separate nested list
    deep = copy.deepcopy(server)

    server["storage"][0] = 750
    print("Original:", server)
    print("Shallow:", shallow)
    print("Deep:", deep)

# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nTODO: Create and test your parent object")
    device1 = ParentClass("Colin's PC", "Online")
    device1.display_info()

    print("\nTODO: Create and test your child object")
    server1 = ChildClass("Server1", "Online", 500, "Office A")
    server1.display_info()
    print("Server capacity:", server1.get_capacity())

    #Student-created extension
    server1.update_status("Offline")
    server1.display_info()

    demonstrate_namespaces()
    demonstrate_copying()

if __name__ == "__main__":
    main()