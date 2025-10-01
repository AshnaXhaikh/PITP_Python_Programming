The `datetime` module is Python's built-in library for handling dates, times, and time intervals. It is extremely powerful and forms the basis for all time-related operations in your code.

Here is a breakdown of the module's core components and the functions most relevant to the code in  `date_formatter.py` file:

### Core Classes in the `datetime` Module

The module defines four main object types:

| Class | Purpose | Example |
| :--- | :--- | :--- |
| **`date`** | Stores year, month, and day. (e.g., 2025-10-01) | `datetime.date(2025, 10, 1)` |
| **`time`** | Stores hour, minute, second, and microsecond. | `datetime.time(14, 30, 0)` |
| **`datetime`** | Combines both `date` and `time`. This is the most commonly used class.  | `datetime.datetime(2025, 10, 1, 23, 19, 5)` |
| **`timedelta`** | Represents a duration, or the difference between two `date` or `datetime` objects. | `datetime.timedelta(days=7, hours=5)` |

***

### Key Functions and Methods (Used in Your Code)

The following methods are essential and appear in your program:

#### 1. `datetime.datetime.now()`

This is a **class method** used to create a new `datetime` object representing the current moment when the function is called.

* **Usage:** `now = datetime.datetime.now()`
* **Purpose:** It gives you a snapshot of the current date and time on the machine running the code.

#### 2. `.strftime(format)`

This is an **instance method** used to convert a `datetime` object into a custom-formatted string.

* **Usage:** `now.strftime("Date: %d-%m-%Y")`
* **Purpose:** It takes a format string as input and replaces the special codes (like `%d`, `%m`, `%Y`) with the actual date and time values from the object. This is what you used to get your standard `01-10-2025` format.

| Format Code | Meaning | Example Output |
| :--- | :--- | :--- |
| `%d` | Day of the month (01-31) | 01 |
| `%m` | Month as a number (01-12) | 10 |
| `%Y` | Year with century (2025) | 2025 |
| `%H` | Hour (24-hour clock) | 23 |
| `%M` | Minute (00-59) | 19 |
| `%S` | Second (00-59) | 05 |
