### 🧩 Difference Between Object and Instance

```python
class Car:
    pass

# Creating objects
car1 = Car()
car2 = Car()

# Checking if they are instances of the class
print(isinstance(car1, Car))  # True
print(isinstance(car2, Car))  # True
```

### 🧠 Explanation:

* `car1` and `car2` are **objects** — they actually exist in memory.
* Both `car1` and `car2` are **instances of the class `Car`** because they were created from it.

So:

* **Objects:** `car1`, `car2`
* **Instances:** The fact that `car1` and `car2` belong to the **Car** class

✅ **In short:**

> “`car1` is an object of the class `Car`, and also an instance of that class.”

---
