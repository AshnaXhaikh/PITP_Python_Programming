#  Object-Oriented Programming Concepts

## 🧩 1. Single Inheritance

**Definition:**
Single inheritance means that a **child class** inherits from **only one parent class**.
This allows the child class to use the properties and methods of that parent.

**Example (Python):**

```python
class Parent:
    def greet(self):
        print("Hello from Parent class!")

class Child(Parent):
    def message(self):
        print("This is the Child class.")

# Object of Child
obj = Child()
obj.greet()     # Inherited from Parent
obj.message()   # Defined in Child
```

**Output:**

```
Hello from Parent class!
This is the Child class.
```

✅ **Key Point:** One child → One parent

---

## 🔗 2. Multiple Inheritance

**Definition:**
Multiple inheritance means a **child class can inherit from more than one parent class**.
This allows it to access attributes and methods from all parent classes.

**Example (Python):**

```python
class Father:
    def skills(self):
        print("Father: Knows driving.")

class Mother:
    def skills(self):
        print("Mother: Knows cooking.")

class Child(Father, Mother):
    def show(self):
        print("Child: Learns both skills.")

# Object of Child
obj = Child()
obj.skills()  # Method Resolution Order (MRO) applies
obj.show()
```

**Output:**

```
Father: Knows driving.
Child: Learns both skills.
```

✅ **Key Point:** One child → Multiple parents
🧠 **MRO (Method Resolution Order):**
If both parents have the same method name, Python runs the one from the **first listed parent**.

---

## 🎭 3. Polymorphism

**Definition:**
Polymorphism means **“many forms”** — the same method name can behave differently for different objects.

**Example (Python):**

```python
class Dog:
    def sound(self):
        print("Dog barks.")

class Cat:
    def sound(self):
        print("Cat meows.")

# Polymorphism in action
for animal in (Dog(), Cat()):
    animal.sound()
```

**Output:**

```
Dog barks.
Cat meows.
```

✅ **Key Point:**
Same method name → Different behavior depending on the object type.

---

### 🧾 Summary Table

| Concept                  | Meaning                                               | Example Relationship         |
| ------------------------ | ----------------------------------------------------- | ---------------------------- |
| **Single Inheritance**   | One child inherits from one parent                    | `Child(Parent)`              |
| **Multiple Inheritance** | One child inherits from multiple parents              | `Child(Father, Mother)`      |
| **Polymorphism**         | Same method behaves differently for different objects | `Dog.sound()`, `Cat.sound()` |

---
