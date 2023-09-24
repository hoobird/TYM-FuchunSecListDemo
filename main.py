####################### Lists in Python ##########################
##################################################################

print("(1): Creating and accessing lists")

# Example 1: Creating a list
fruits = ["apple", "banana", "cherry", "orange", "grape"]
print("Fruits:", fruits)

# Example 2: Accessing elements in a list
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

print()

print("(2): Modifying lists")

# Example 1: Changing an element in a list
print("Fruits before modification:", fruits)
fruits[0] = "strawberry"
print("Fruits after modification:", fruits)

# Example 2: Adding an element to a list (append)
fruits.append("watermelon")
print("Fruits after appending:", fruits)

# Example 3: Inserting an element in a list (insert)
fruits.insert(2, "kiwi")
print("Fruits after inserting:", fruits)

# print()

print("(3): Removing elements from lists")

# Example 1: Removing an element by value (remove)
fruits.remove("cherry")
print("Fruits after removing cherry:", fruits)

# Example 2: Removing an element by index (pop)
fruits.pop(1)
print("Fruits after popping index 1:", fruits)

# Example 3: Removing a range of elements (del)
del fruits[1:3]
print("Fruits after deleting a range:", fruits)

print()

print("(4): List methods and functions")

# Example 1: Length of a list (len)
print("Length of fruits:", len(fruits))

# Example 2: Reversing a list (reverse)
print("Fruits list before reversing:", fruits)
fruits.reverse()
print("Reversed fruits:", fruits)

# Example 3: Sorting a list (sort)
print("Fruits list before sorting:", fruits)
fruits.sort()
print("Sorted fruits:", fruits)
