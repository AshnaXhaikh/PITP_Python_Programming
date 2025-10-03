# 🐍 Exception Handling in Python

Exception handling in Python allows you to deal with runtime errors gracefully instead of letting the program crash.

---

## 📌 What is an Exception?

An **exception** is an error that occurs during program execution, which interrupts the normal flow of instructions.
Instead of crashing, Python allows us to **handle exceptions gracefully**.

---

## ⚡ Commonly Used Exceptions

* **ZeroDivisionError** → Division by zero
* **ValueError** → Invalid value (e.g., converting "abc" to int)
* **TypeError** → Wrong data type used in operation
* **FileNotFoundError** → Trying to open a missing file
* **IndexError** → List index out of range
* **KeyError** → Dictionary key not found
* **NameError** → Using a variable that is not defined

---

## 🛠️ Using try-except

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")
```

---

## 🧩 Multiple except Blocks

```python
try:
    num = int("hello")
except ValueError:
    print("Invalid number format")
except TypeError:
    print("Type mismatch occurred")
```

---

## 🎯 Using finally

The `finally` block always executes, whether an exception occurs or not.
It is useful for cleanup tasks like closing files or releasing resources.

```python
try:
    f = open("data.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution finished")
```

---

## 🚀 Raising Exceptions

We can raise exceptions manually using `raise`:

```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print("Valid age:", age)

try:
    check_age(-5)
except ValueError as e:
    print("Error:", e)
```

---

## 📚 Summary

* **try** → Write code that might throw an error
* **except** → Handle the error
* **finally** → Always runs (cleanup, close resources)
* **raise** → Manually trigger an exception

---

✅ With exception handling, our code becomes more **robust, reliable, and user-friendly**.

---
