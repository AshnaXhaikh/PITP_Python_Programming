"""This file defines the function to format student information."""
def student_info(name, age, grade):
    """Returns a formatted string with studnt details."""
    info_string = (
        f"---Student Details---\n"
        f"Name: {name}\n"
        f"Age: {age}\n"
        f"Grade: {grade}\n"
    )
    return info_string