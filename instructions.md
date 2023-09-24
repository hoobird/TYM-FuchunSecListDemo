# Lists in Python

## Instructions
- Follow the instructor's walkthrough to learn about Lists and how to use them.
- Execute the code in `main.py` file to see the output after manipulation on the list we created.
- Comment and uncomment lines of code easily with the shortcuts:
  1. Windows - `Ctrl` and `/`
  2. Mac - `Cmd` and `/`
- After the instructor has walk through the Lists demo, proceed to attempt Exercises on Lists

## Overview

- A list in Python is a versatile, mutable, and ordered collection of items.
- Lists are enclosed in square brackets `[ ]`, and elements are separated by commas `,`.
- Lists can contain different types of data: numbers, strings, objects, and even other lists.

## Lists Methods 

### Creating and Accessing Lists

#### Creating a List

A list can be created by enclosing elements in square brackets `[]` and separating them with commas `,`.

```python
fruits = ["apple", "banana", "cherry", "orange", "grape"]
```

#### Accessing Elements

Elements can be accessed using their index. The index starts from 0 for the first element.

```python
print(fruits[0])  # Outputs: "apple"
print(fruits[-1])  # Outputs: "grape"
```

### Modifying Lists

#### Changing an Element

An existing element in the list can be modified using its index.

```python
fruits[0] = "strawberry"
```

#### Adding an Element

You can add an element at the end of the list using `append()` or at a specific index using `insert()`.

```python
fruits.append("watermelon")
fruits.insert(2, "kiwi")
```

###  Removing Elements

#### Removing by Value

An element can be removed from the list by its value using `remove()`.

```python
fruits.remove("cherry")
```

#### Removing by Index

An element can also be removed by its index using `pop()`.

```python
fruits.pop(1)
```

#### Removing a Range of Elements

A range of elements can be removed using the `del` statement.

```python
del fruits[1:3]
```

###  List Methods and Functions

#### Length of a List

The length of a list can be obtained using `len()`.

```python
print(len(fruits))
```

#### Reversing a List

A list can be reversed using `reverse()`.

```python
fruits.reverse()
```

#### Sorting a List

A list can be sorted in ascending order using `sort()`.

```python
fruits.sort()
```
