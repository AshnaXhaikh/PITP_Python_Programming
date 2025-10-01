A Python package is just a directory containing a special file named __init__.py. This structure allows you to organize and import related modules (like circle.py or student.py) from other files.

    Here is the guide for the required folder structure and file contents for both tasks:

    ```
    project_root/
    ├── task1/
    │   ├── shapes/ # Package directory
    │   │   ├── __init__.py # Marks this directory as a package 
    │   │   ├── circle.py # Module containing the area function
    │   ├── main_shapes.py # Main program to use the shapes package     
    ├── task2/
    │   ├── school/ # Package directory
    │   │   ├── __init__.py # Marks this directory as a package
    │   │   ├── student.py # Module containing the student_info function
    │   ├── main_school.py # Main program to use the school package
    ```
    Each task folder contains a package directory with an __init__.py file, a module file with the required function, and a main program file that imports and uses the package.
    