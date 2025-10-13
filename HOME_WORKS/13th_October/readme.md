## 📘 Key Concepts & Definitions

| Concept | Definition | Use Case in Homework |
| :--- | :--- | :--- |
| **Dictionary** | An **unordered** collection of data stored as **Key-Value pairs**. Keys must be unique and immutable. | Storing friend-color pairs, country-capital pairs, and product details. |
| **Set** | An **unordered** collection of **unique** elements. Used for membership testing and eliminating duplicates. | Finding unique emails, performing union/intersection, and calculating set differences. |
| **List** | An **ordered** and **changeable** collection of items. Allows duplicate members and supports indexing. | Storing ordered daily temperatures for calculating an average. |

---

## 📝 Homework Breakdown

### a. Key-Value Pairs (Dictionaries)
Focused on fundamental dictionary manipulation:
* Creating, accessing, and iterating through key-value pairs.
* Dynamically **adding** a new pair and **removing** an existing one.
* Using `len()` to count the total number of keys.

### b. Dictionary Methods
Explored built-in methods for efficient dictionary management:
* `.keys()`: Returns a view object that displays a list of all keys in the dictionary.
* `.pop()`: Removes the item with the specified key and returns its value.
* `.clear()`: Removes all items from the dictionary.
* `.get()`: Safely retrieves a value by key, returning `None` (or a specified default) if the key isn't found, preventing a `KeyError`.

### c. Set Operations
Demonstrated how sets are used for mathematical operations and ensuring uniqueness:
* **Union** (`|` or `.union()`): Returns a new set containing all items from both sets (all odd and even numbers).
* **Intersection** (`&` or `.intersection()`): Returns a set containing only items present in *both* sets.
* **Difference** (`-` or `.difference()`): Returns a set containing items from the first set that are not found in the second.

### d. Data Structure Use Cases
Applied the structures to practical, real-world problems:
* **List Average:** Calculated the sum of a list of daily temperatures and divided by the list's length (`len()`) to find the average.
* **Product Details:** Used a **dictionary** to group a product's attributes (**name**, **price**, **quantity**) logically.
* **Deduplication:** Converted a list of emails to a **set** to instantly remove duplicates, leveraging the set's inherent uniqueness property.
