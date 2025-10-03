# 🐍 Exception Handling in Python

## 📌 What is an Exception?

An **exception** is an error that occurs during program execution, which interrupts the normal flow of instructions.
Instead of crashing, Python allows us to **handle exceptions gracefully**.

---

## ⚡ Common Exceptions

* `ZeroDivisionError` → Division by zero
* `ValueError` → Invalid type of value
* `TypeError` → Invalid operation between different data types
* `FileNotFoundError` → Missing file
* `IndexError` → List index out of range
* `KeyError` → Dictionary key not found

---

## 🛠️ Basic Syntax

```python
try:
    # Code that might cause an error
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
```

---

## 🧩 Multiple Except Blocks

```python
try:
    num = int("hello")
except ValueError:
    print("Conversion failed: Invalid number")
except TypeError:
    print("Wrong type used")
```

---

## 🎯 Flow of try-except-else-finally

```
 ┌───────────┐
 │   try     │  → Run risky code
 └─────┬─────┘
       │
       ▼
   Exception? ────► Yes ─► Go to except block
       │
       No
       ▼
     else block (runs if no error)
       ▼
   finally block (always runs)
```

---

## 🎯 Using else and finally

```python
try:
    f = open("data.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found!")
else:
    print("File read successfully")
finally:
    print("Closing the program")
```

---

## 🔄 Raising Exceptions

```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    check_age(-5)
except ValueError as e:
    print("Error:", e)
```

---

## ✅ Best Practices

✔ Catch **specific exceptions**
✔ Provide **meaningful error messages**
✔ Use **finally** for cleanup (files, DB connections)
✔ Avoid bare `except:` (too broad)
✔ Use `with` for resource management

---

## 📚 Summary

* **try** → Code that might fail
* **except** → Handle the error
* **else** → Run if no error
* **finally** → Always run (cleanup)
* **raise** → Manually trigger an exception

---

👉 This makes our code more **robust, safe, and professional**.
