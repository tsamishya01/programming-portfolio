WEEK 2 SUMMARY:

This lecture focused on the fundamental concepts of variables and data types in Python, which are essential for writing meaningful and functional programs. It introduced how Python stores data using variables, how different data types behave, and how user input, functions, and collections such as lists are handled. Through practical exercises, students learned how Python dynamically assigns data types, manipulates values, and processes input and output efficiently. These concepts form the foundation for more advanced programming topics such as control structures, functions, and data structures 
 
Exercise-2 Variables and Types

KEY TECHNOLOGIES & CONCEPTS LEARNED:

Python Programming Language

Variables and Assignment

Primitive Data Types (int, float, string, boolean)

Dynamic Typing

Built-in Functions (print(), input(), type(), max(), len())

Augmented Assignment Operators (+=, *=)

String Handling and Escape Sequences

Lists and Mutability

Indexing and Slicing

User Input and Output

Type Conversion and Expressions

KEY NOTES:

A variable is used to store data values that can change during program execution.

Python uses dynamic typing, meaning the data type is determined at runtime based on the assigned value.

Common data types include:

Integer (int) – whole numbers

Float (float) – decimal numbers

String (str) – text data

Boolean (bool) – True or False

The type() function is used to check the data type of a variable.

The input() function always returns user input as a string, requiring type conversion for numerical operations.

Augmented assignment operators simplify updating variable values.

Strings support indexing and slicing, allowing access to specific characters or substrings.


WEEK 3 SUMMARY:

This lecture explains how programs make decisions and repeat actions using control statements in Python. Earlier, programs only ran line by line, but this lecture shows how to add logic to programs. Students learned how to use conditions, loops, and Boolean expressions to control the flow of a program. These concepts help in writing real-world programs that can think, decide, and repeat tasks automatically.

KEY NOTES:

Programs work using sequence, selection, and iteration.

Boolean expressions always give True or False.

Comparison operators like <, >, ==, != are used in conditions.

The if statement checks a condition and runs code only if it is true.

else runs when the if condition is false.

elif is used to check multiple conditions.

Logical operators:

and → all conditions must be true

or → at least one condition must be true

not → reverses the result

Python allows chained comparisons, like 10 < x <= 50.

Membership testing checks if a value exists in a list or string.

Non-boolean values can also act as conditions:

0 or empty values → False

Non-zero or non-empty values → True

The ternary operator is a short form of if–else that returns a value.

while loop repeats as long as a condition is true.

for loop repeats over a sequence like a list or range.

range() generates numbers for loops.

WEEK 4 SUMMARY:

This lecture explains what functions are and why they are important in Python programming. Functions help us reuse code, keep programs organized, and make them easier to understand. Students learned how to use built-in functions, import functions from modules, and create their own functions. The lecture also introduced advanced concepts such as default arguments, keyword arguments, variable-length arguments, and lambda expressions, which help write flexible and efficient programs.

KEY TECHNOLOGIES AND CONCEPTS LEARNED:

Python functions

Built-in functions

Importing modules and functions

Python Standard Library

User-defined functions

Parameters and arguments

Return values

Default arguments

Keyword arguments

Variable-length arguments (*args)

Arbitrary keyword arguments (**kwargs)

Lambda (anonymous) functions

KEY NOTES:

Functions are blocks of code that perform a specific task.

Python has many built-in functions like print(), input(), range(), and type().

Extra functions are stored in modules and must be imported before use.

Example: import math allows use of math functions like math.sqrt().

Specific functions can be imported using from module import function.

Functions are defined using the def keyword.

A function can take parameters and return a value using return.

Variables inside a function are local and cannot be used outside.

If no value is returned, the function returns None.

Docstrings describe what a function does and help in documentation.

Default arguments allow calling a function without giving all values.

Keyword arguments allow passing values using parameter names.

Functions can accept any number of arguments using *args.


KEYNOTES:

Scripts vs. Modules: Working in interactive mode is good for small snippets, but substantial programs are stored in text files called scripts (p. 3). These files, with a .py suffix, can be executed by the Python interpreter (e.g., python my_program.py) (pp. 3-4). Any .py file containing definitions and statements can also be imported as a module into other programs.
Command Line Arguments: Arguments can be passed to a script upon execution and are accessed within the program via the sys.argv list (p. 5). The first element of sys.argv is the script's filename.
Importing:
Whole Module: import math creates a variable math in the local symbol table, and functions must be prefixed (e.g., math.sqrt(x)).
Aliasing: import math as m allows a shorter or different name to be used as a prefix (e.g., m.sqrt(x)).
Specific Elements: from math import sqrt, pi imports specific names directly into the local symbol table, requiring no prefix.
Wildcard Import: from math import * imports all content, but is generally discouraged due to potential name clashes.
Module Search Path: When a module is imported, Python checks for built-in modules first, then searches the directories listed in the sys.path variable (p. 13). This list is initialized to include the script's directory and the PYTHONPATH environment variable.
The name Variable: 

WEEK 6 SUMMARY:

List Manipulation: Exercises cover the use of list methods such as reverse(), append(), pop(), remove(), insert(), count(), and index().
Mutability: The document asks about the difference between mutable (lists) and immutable (tuples) data types, and how methods change them .
Accessors vs. Mutators: Questions require identifying whether specific methods are accessors (read-only) or mutators (changers).
List Comprehensions and Loops: There are tasks involving writing for loops to iterate over lists and creating lists using list comprehensions .

KEY POINTS:
Mutability Distinction: The core concept is that Python lists are mutable (changeable after creation), while tuples are immutable (cannot be changed after creation).
Syntax: Lists are defined using square brackets [] and tuples use parentheses (). A single-element tuple requires a trailing comma, e.g., (1,).
List Methods: The exercises utilize methods that modify lists in-place (mutator methods), such as append(), extend(), insert(), remove(), pop(), reverse(), and sort().
Tuple Methods: Because tuples are immutable, they have fewer methods; the exercises focus on accessor methods that return information without changing the tuple, such as count() and index().
Accessors vs. Mutators: An accessor method reads a value (e.g., index()), while a mutator method changes the data structure (e.g., append()).
Iteration and Comprehension: Both lists and tuples can be iterated over using for loops, and lists can be generated concisely using list comprehensions.

WEEK 7 SUMMARY:
Sets as Unordered Collections: Sets are unordered collections of unique elements; they do not support indexing or slicing because items have no fixed position.
Set Mutability: Regular sets (set()) are mutable data types, allowing elements to be added or removed (p. 2). A frozenset() is an immutable version .
Set Operations: Mathematical set operations covered include the & operator for intersection and the pipe | for union .
Set Comprehensions: Sets can be programmatically populated using comprehension syntax .

KEY POINTS:
Sets as Unordered Collections: Sets are unordered collections of unique elements, which means they do not support indexing or slicing because items have no fixed position .
Set Mutability: Regular sets (set()) are mutable data types, allowing elements to be added or removed. A frozenset() is an immutable version that can be used where unchangeable data is required, such as in another set or as a dictionary key.
Set Operations & Operators: Mathematical set operations use specific operators, such as the & for intersection (common elements) or the pipe | for union (all elements).

WEEK 8 SUMMARY:
Sets as Unordered Collections: Sets are unordered collections of unique elements; they do not support indexing or slicing because items have no fixed position.
Set Mutability: Regular sets (set()) are mutable data types, allowing elements to be added or removed (p. 2). A frozenset() is an immutable version .
Set Operations: Mathematical set operations covered include the & operator for intersection and the pipe | for union .
Set Comprehensions: Sets can be programmatically populated using comprehension syntax .
Dictionaries as Key-Value Pairs: Dictionaries store data as a mapping of unique keys to values, referred to as key-value pairs .
Dictionary Properties: Dictionaries are mutable, but their keys must be of an immutable type. Values do not need to be unique.
Accessing and Iterating Dictionaries: Values are accessed using square brackets with the corresponding key (e.g., stock["banana"]). Iteration can occur over keys or values using for loops.




KEY POINTS:

Sets as Unordered Collections: Sets are unordered collections of unique elements, which means they do not support indexing or slicing because items have no fixed position .
Set Mutability: Regular sets (set()) are mutable data types, allowing elements to be added or removed. A frozenset() is an immutable version that can be used where unchangeable data is required, such as in another set or as a dictionary key.
Set Operations & Operators: Mathematical set operations use specific operators, such as the & for intersection (common elements) or the pipe | for union (all elements).
Dictionaries as Key-Value Pairs: Dictionaries store data as a mapping of unique keys to values, a pairing often referred to as key-value pairs.
Dictionary Properties: Dictionaries are mutable, but their keys must be of an immutable type (like strings or numbers). Values do not need to be unique.
Accessing and Iterating Dictionaries: Values are accessed using square brackets with the corresponding key (e.g., stock["banana"]). Iteration can be done over.
