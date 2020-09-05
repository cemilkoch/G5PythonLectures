# Python

Python is a dynamic, interpreted (bytecode-compiled) language. At the time of this writing, python is the fastest growing and most popular programming language. It is most often used by software engineers, mathematicians , data analysts, scientists, network engineers and even accountants! Most people who are not software engineers love to use python for automation purposes. With all this being said, python is simply a multipurpose language. 

### Python Interpreter

CPython interpreter is the reference implementation of Python which is written in C. This interpreter is turned into machine code with something like gcc and executed directly on the CPU. This machine code then reads textual data from our .py file and causes the appropriate computation to process the python statements. To understand exactly how this work, go to this [link!](https://www.youtube.com/watch?v=KsZLPTRSleI)

### Python 2 vs Python 3

Python 2 and Python 3 are quite different. To the point that Python 3 is not “backwards-compatible” which means that if you have a project that is using various Python 2 libraries they may no longer work after you upgrade. There are multiple difference between python 2 and python 3 in terms of syntax which is msotly responsible for the lack of “backwards-compatibility”. Its best to simply stick to python 3 unless you plan to use older libraries that were first implemented in python 2. 

### Pip3

Pip is the standard package manager for python. Using it allows you to install packages that are not part of the standard library. Pip3 is a version of the pip installer for python3, which can download and configure new python modules too. Pip3 relies on PyPI ([the Python Package Index](https://pypi.org/)) which is a [software repository](https://en.wikipedia.org/wiki/Software_repository) where versions of community-managed modules are maintained.

### __pycache__ ?

This is where lives Python 3 bytecode compiled and ready to be executed. You normally want to add this into your gitignore file. This is simply bytecode cerated when you compile your python code. Which means that it can be re-obtained once you compile python again.  

### Python Reserved Words

You cannot used reserved words as variable names/identifiers

-and
-except
-lambda
-with
-as
-finally
-nonlocal
-while
-assert
-false
-None
-yield
-break
-for
-not
-class
-from
-or
-continue
-global
-pass
-def
-if
-raise
-del
-import
-return
-elif
-in
-True
-else
-is
-try

### Rules for writing identifiers

1. Identifiers can be a combination of letters in lowercase **(a to z)** or uppercase **(A to Z)** or digits **(0 to 9)** or an underscore `_`. Names like `myClass`, `var_1` and `print_this_to_screen`, all are valid example.

2. An identifier cannot start with a digit. `1variable` is invalid, but `variable1` is a valid name.

3. Keywords cannot be used as identifiers.

      ```python
      global = 1
      ```

      **Output**
      ```python
            File "<interactive input>", line 1
            global = 1
            ^
            SyntaxError: invalid syntax
      ```

4. We cannot use special symbols like **!, @, #, $, % etc.** in our identifier.

      ```python
            a@ = 0
      ```

      **Output**
      ```python
            File "<interactive input>", line 1
            a@ = 0
            ^
            SyntaxError: invalid syntax
      ```

5. An identifier can be of any length.
