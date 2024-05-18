

Step-by-Step Guide to Developing Your AirBnB Clone

First Step: Build a Command Interpreter

Your journey towards creating a full-fledged web application begins with writing a command interpreter for managing AirBnB objects. This foundational step is crucial as it will lay the groundwork for subsequent projects including HTML/CSS templating, database storage, API integration, and front-end development.

Objectives
1. Implement a Parent Class:
Create a BaseModel class responsible for initializing, serializing, and deserializing instances.

2. Serialization/Deserialization Flow:
Establish a simple serialization/deserialization flow: Instance <-> Dictionary <-> JSON String <-> File.

3. Create Essential Classes:
Develop classes like User, State, City, and Place that inherit from BaseModel.

4. Storage Engine:
Implement the first abstracted storage engine: File Storage.

5. Unit Testing:
Write unittests to validate all classes and the storage engine.

Command Interpreter Overview
A command interpreter functions similarly to a shell but is tailored for specific use cases. Here, it will manage project objects:

Create a new object (e.g., a new User or Place).
Retrieve objects from storage (file, database, etc.).
Perform operations on objects (count, compute stats).
Update object attributes.
Delete objects.
The interpreter should also support non-interactive mode, ensuring compatibility with automated scripts.

Execution
The shell should function in both interactive and non-interactive modes:

Interactive Mode:
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  nothing  quit  show  update

(hbnb) quit
$

Non-Interactive Mode:

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)


Detailed Tasks:

1. README and AUTHORS:

Write a README.md describing the project and command interpreter usage.
Create an AUTHORS file listing all contributors.

2. PEP8 Compliance:

Ensure all code adheres to PEP8 standards.

3. Unit Tests:

Test all files, classes, and functions using unittests.
Ensure tests pass in both interactive and non-interactive modes.

4. BaseModel Class:

Implement BaseModel with attributes (id, created_at, updated_at) and methods (save, to_dict).

5. Dictionary Representation:

Develop functionality to create instances from dictionary representations.

6. Store Objects:

Implement object storage and retrieval using JSON files.

7. Command Interpreter 0.0.1:

Develop console.py with basic commands (quit, EOF, help).

8. Command Interpreter 0.1:

Extend console.py with commands (create, show, destroy, all, update).

9. User Class:

Create a User class with attributes (email, password, first_name, last_name).

10. Additional Classes:

Develop classes State, City, Amenity, Place, and Review inheriting from BaseModel.

11. Update Storage:

Modify storage to handle all new classes correctly.

12. All Instances by Class:

Add functionality to retrieve all instances of a class.

13. Instance Count:

Implement a command to count instances of a class.

14. Show Instance:

Add functionality to retrieve an instance by its ID.

15. Destroy Instance:

Implement instance deletion by ID.

16. Update Instance:

Add functionality to update instance attributes by ID.

17. Update from Dictionary:

Enable instance updates using a dictionary of attributes.

Contributors:

1. Joseph Eke...............................
