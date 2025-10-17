# OOP Concepts in Python

Object-Oriented Programming (OOP) is a programming paradigm that organizes code using **classes** and **objects**. Python supports OOP, making it easier to model real-world entities.

This README explains the fundamental concepts: **class, object, instance, attributes, methods, `self`, and `__init__`**.

---

## 1. Class

A **class** is a blueprint for creating objects. It defines the structure (attributes) and behavior (methods) that the objects will have.

**Example:**

```python
class Person:
    pass
```

---

## 2. Object

An **object** is a specific instance of a class. It represents an entity with real values for the attributes defined in the class.

**Example:**

```python
person1 = Person()
```

---

## 3. Instance

An **instance** is another term for an object. Each object created from a class is an instance of that class.

**Example:**

```python
person2 = Person()  # person2 is another instance of the Person class
```

---

## 4. Attributes

**Attributes** are variables that store data about an object. They define the properties of the object.

**`__init__` method:**

* A special method called when an object is created.
* Used to initialize object attributes.

**`self` keyword:**

* Refers to the current instance of the class.
* Allows access to the object’s attributes and methods.

**Example:**

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age    # attribute

person = Person("Alice", 25)
print(person.name)  # Output: Alice
```

---

## 5. Methods

**Methods** are functions defined inside a class that describe the behavior of objects. They can access or modify object attributes using **`self`**.

**Example:**

```python
class Person:
    def __init__(self, name):
        self.name = name  # attribute

    def greet(self):
        print(f"Hello, my name is {self.name}")  # using self to access attribute

person = Person("Alice")
person.greet()  # Output: Hello, my name is Alice
```

---

## Summary Table

| Concept    | Definition                                     |
| ---------- | ---------------------------------------------- |
| Class      | Blueprint for creating objects                 |
| Object     | A specific instance of a class                 |
| Instance   | A single occurrence of an object               |
| Attributes | Data stored in an object                       |
| Methods    | Functions that define object behavior          |
| `__init__` | Special method to initialize object attributes |
| `self`     | Refers to the current object instance          |

---
