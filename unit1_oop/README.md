# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

## Unit 1 Reflection

The most useful aspect of this assignment was getting a glimpse into how inheritance, namespaces, and copying work together in Python. I was able to practice class and instance variables, inheritance with super(), and overriding methods using computer objects and server objects. The namespace demo also illustrated how classes can share common variables, but have individual properties.

There were some problems with shallow and deep copies. An error occurred when I attempted to use the copying functions, but the fix was simple. All I had to do was adjust my import statement. When it worked, I could see that the shallow copy was pointing to the same list as the original dictionary, whereas the deep copy is pointing to a different list.

The benefits of using OOP over procedural programming are that classes can be used to group related data and functions together. Inheritance can be used to reuse and extend pre-existing functionality without repeating the code in multiple parts of a program. This can help the development process with organization, reduce overheads, and make future changes easier to manage. For smaller programs with less involved tasks, however, the added structure might not be required.