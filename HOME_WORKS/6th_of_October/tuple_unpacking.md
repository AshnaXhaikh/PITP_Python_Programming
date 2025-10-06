# 🐍 Tuple Unpacking in Python

## 📘 What is Tuple Unpacking?

Tuple unpacking means assigning **multiple values to multiple variables** in a **single line** using commas.

---

🎯 In simple terms:

👉 Right side packs values into a tuple
👉 Left side unpacks them back into variables

It’s like:

> “Pack values together → then unpack them into new places.”

---

## 🧩 Basic Example

```python
x, y = 5, 10
print(x)  # 5
print(y)  # 10
```

### 🔍 What happens here?

* The right side `5, 10` forms a tuple → `(5, 10)`
* Then Python **unpacks** it into the left side:

  * `x` gets 5
  * `y` gets 10

---

## 🔁 Swapping Variables Easily

Tuple unpacking makes swapping very easy — no need for a temporary variable!

```python
a = 3
b = 7
a, b = b, a
print(a, b)  # 7 3
```

---

## 🔄 Swapping Three Variables

You can even swap three or more variables at once:

```python
a, b, c = 1, 2, 3
a, b, c = c, a, b
print(a, b, c)  # 3 1 2
```

### 🧠 Explanation:

Right side → creates a tuple `(c, a, b)`
Left side → unpacks the tuple and reassigns values

---

## 🧺 Unpacking a Tuple Variable

You can also unpack from an existing tuple:

```python
point = (4, 5)
x, y = point
print(x)  # 4
print(y)  # 5
```

---

## ⚙️ Using `*` (Star) for Extended Unpacking

```python
numbers = (1, 2, 3, 4, 5)
a, *b, c = numbers
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5
```

---

## ✅ Summary

* **Tuple unpacking** assigns multiple values at once.
* It works with **any iterable** (tuple, list, string, etc.).
* Useful for **swapping**, **multiple returns**, and **cleaner code**.

---


