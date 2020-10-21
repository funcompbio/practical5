---
layout: page
title: Practical 5
permalink: /practical5/
---

# Objectives

The learning objectives for this practical are:

 * Implement a program in Python that decides if two given numbers are relatively primes.
 * Implement a program in Python that decides if a given number is cool.
 * Execution modes in Python.
 * How to take arguments from the command line.
 * Make syntax errors in Python.
 * Correct syntax errors in Python.
 * Debug your program when it doesn't work.

For the problems in which you have to implement a program that
solves some arithmetic problem that we have solved in class at the
blackboard, you should have already one working solution from that class
on paper. If you don't, please ask a colleague for one. Try
to focus the time of this practical in addressing the technical challenges
of running a Python program and correcting run-time errors.

Whenever you are stuck with an error, please consult the section
entitled "Debugging" from [practical 4](/practical4/).

# Setup and background

To do this practical you need an installation of Python version 3. You can find
the instructions in the [setup](/setup/) link on how to install Python version 3
in your system. Once Python is installed, you should be able to call it from
the shell in the terminal window. You can check whether that is possible by typing:

```
$ which python
$ python --version
```

It may happen that you have two Python installations, one corresponding
to version 2.x and another to version 3.x. In that situation the previous command
may say that your Python version is 2.x and to access the version 3 you need to call
the executable `python3`. Try then for instance:

```
$ python3 --version
```

If this is your case, then whenever the executable `python` is invoked in the rest of
this practical, please use `python3` instead.

# Relatively prime numbers

The Wikipedia [page](https://en.wikipedia.org/wiki/Coprime_integers) for relatively
prime numbers says:

> In number theory, two integers a and b are relatively prime, mutually prime, or coprime if the only positive integer that evenly divides (is a divisor of) both of them is 1. One says also a is prime to b or a is coprime with b. Consequently, any prime number that divides one of a or b does not divide the other. This is equivalent to their greatest common divisor (gcd) being 1.

Implement a program in Python that asks for two positive integer numbers and says whether
they are relatively prime or not, providing some message with the `print()` function.

# Cool numbers

We say that a positive integer number `x` is **cool** if this number is equal to the sum of
any sequence of increasing consecutive positive integer numbers smaller or equal than `x`,
starting on 1. For instance, number 1 is cool because the only positive integer number
smaller or equal than 1 is 1 itself; number 2 is not cool because neither 1 nor 1+2 are
equal to 2; number 3 is cool because 3=1+2. Until 10, numbers 4, 5, 7, 8 and 9 are not cool.
However, 6=1+2+3 and 10=1+2+3+4 are indeed cool.

Implement a program in Python that asks for one positive integer number and says whether
the given number is cool or not, providing some message with the `print()` function.

# Execution modes in Python

This section requires to first read slides 9 to 16 from the lecture on
[Programming with Python (2)](/lecture5/).

There are three main ways in which you can run a Python program:

1. Running it from the Unix shell command line.

2. Interactively, through the Python shell interpreter.

3. Importing Python code into another Python program.

Actually, the first two ways are equivalent and only the third one is qualitatively
different from the first two. To understand that difference we need to learn that Python defines
for us a variable called [`__name__`](https://docs.python.org/3/library/__main__.html),
in which Python stores the name of the _scope_ in which top-level code executes. This
_scope name_ will be either the name of the module to which the code belongs to when running
in the previously described situation (3), or the value `__main__`, when running in the
previously described situations (1) or (2).

Create a text file called `thismodule.py` and put the following line on it:

```
print("__name__: %s" %(__name__))
```

Now let's call this Python script from the Unix shell command line:

```
$ python thismodule.py 
__name__: __main__
```

We can see that when calling the Python script `thismodule.py` from the Unix shell
command line, the `__name__` variable takes the value `__main__`. Now start the
Python shell interpreter (calling `python` or `python3` from the Unix command line
without arguments), directly type the `__name__` variable and hit the `Enter` key:

```
>>> __name__
`__main__`
```

We also see here that in the Python interactive prompt `__name__` takes the value
`__main__`. Finally, from this same prompt let's import the code in `thismodule.py`
as if we were importing it in some other Python script:

```
>>> import thismodule
__name__: thismodule
```

Differentely to the previous two execution modes, when importing Python code as
 a module, the `__name__` variable takes the value of the module name.

# How to take arguments from the command line.

We have seen in the previous section that the `__name__` variable allows us to
detect in our Python code when it is executing from the Unix shell command line.
In this particular execution mode, we can use the Python module `sys` to fetch
argument values given by the user in the command line. To illustrate this
functionality, edit the previous file `thismodule.py` and add the following lines:

```
if __name__ == "__main__" :
  import sys
  i = 0
  while i < len(sys.argv) :
    print("argument vector position %d: %s" %(i, sys.argv[i]))
    i = i + 1
```

If you call this script in the Unix command line with the arguments
`give me 5` you should be getting the following output:

```
$ python thismodule.py give me 5
__name__: __main__
argument vector position 0: thismodule.py
argument vector position 1: give
argument vector position 2: me
argument vector position 3: 5
```

Try to understand what are the contents of the vector `argv` in the
module `sys` in the previous execution mode. Once you have understood
that, try to complete the following exercise.

Make a new version of the Python program that decides whether two
positive integer numbers are relatively prime with the following
characteristics:

1. Instead of asking the user to enter two values, it should take them
from the Unix command-line arguments.

2. The code doing the actual calculation on whether two given numbers
are relatively prime should be encapsulated into a function called
`main(x, y)` with two arguments `x` and `y` corresponding to the two
numbers to be evaluated. This function should return a character string
value set to `yes` when `x` and `y` are relatively prime and `no` when
they are not. This function should not print anything on the screen.

3. When the script is called from the command line without the two
arguments corresponding to the two positive integer values to evaluate,
then for a script called, e.g., `relprime.py`, the user should get a
message like:

```
$ python relprime.py
error: relprime.py <x> <y>
```

4. When the script is properly called from the command line with the two
arguments corresponding to the two positive integer values to evaluate,
then the script should call the previously defined `main(x, y)` function,
take its result and print it in the terminal screen.
