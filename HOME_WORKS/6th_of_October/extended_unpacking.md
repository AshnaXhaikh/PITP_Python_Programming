## 🧩 What is Extended Unpacking?

Normally, tuple unpacking works when the **number of variables = number of values**.
Example:

```python
a, b, c = (1, 2, 3)
```

✅ Works perfectly — 3 variables, 3 values.

But what if there are **more values** than variables?
Example:

```python
a, b = (1, 2, 3, 4)
```

❌ This gives an error — “too many values to unpack”.

---

## 🌟 Extended Unpacking Solves This

Python lets you use a **star (`*`) operator** to grab *multiple values* into a list.

Example:

```python
a, *b, c = (1, 2, 3, 4, 5)
```

### 💡 What happens:

* `a` → gets `1`
* `b` → collects the **middle values** `[2, 3, 4]`
* `c` → gets `5`

So after unpacking:

```python
a = 1
b = [2, 3, 4]
c = 5
```

---

## 🧠 You can use it anywhere:

### 1️⃣ At the start

```python
*a, b = [10, 20, 30, 40]
print(a)  # [10, 20, 30]
print(b)  # 40
```

### 2️⃣ At the end

```python
a, *b = [10, 20, 30, 40]
print(a)  # 10
print(b)  # [20, 30, 40]
```

### 3️⃣ With nested structures

```python
data = ("Ashna", 20, "AI", "Python", "ML")
name, age, *skills = data
print(name)    # Ashna
print(age)     # 20
print(skills)  # ['AI', 'Python', 'ML']
```

---

## ✅ Summary

| Symbol      | Meaning                                         | Example                |
| ----------- | ----------------------------------------------- | ---------------------- |
| `*`         | Collects multiple values into a list            | `a, *b, c = (1,2,3,4)` |
| Without `*` | Number of variables must match number of values | `a, b = (1,2)` ✅       |

---

So basically:

> **Extended unpacking** allows you to “catch the rest” of the values easily.

---