---
layout: page
title: Practical 5
permalink: /practical5/
---

# Objectives

The learning objectives for this practical are:

 * Implement a program in Python that decides if two given numbers are relatively prime.
 * Implement a program in Python that decides if a given number is cool.
 * Bundling lines together into functions.
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
entitled "Debugging" from [practical 4](/practical4#debugging).

# Setup and background

To do this practical you need an installation of Python version 3. You can find
the instructions in the [setup](/setup#python-and-jupyter-notebook/) link on how to install Python version 3
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
this practical, please use `python3` instead. Make a directory for this practical,
called `practical5`, and store there the files generated during the practical.

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

# Bundling lines together into functions

Programming instructions performing a specific task, such as the calculation
of a particular value or decision, can be bundled together under a so-called
[function](https://en.wikipedia.org/wiki/Subroutine); see the slides on
functions from [this lecture](https://funcompbio.github.io/lecture5/#11).

Edit the previous two programs and, in each of them, bundle together the
code into a function called `main()` and put a call to that function
`main()` at the bottom of the file, i.e.:

```
def main() :
  ## CODE OF YOUR PYTHON PROGRAM
  ## INDENTED TO BECOME BUNDLED
  ## INTO A FUNCTION CALLED main()
  ## THIS IS THE SO-CALLED "BODY"
  ## OF THE FUNCTION

main() ## THIS IS THE "CALL" TO THE FUNCTION main()
```
Verify that the program runs in exactly the same way as before you did
these modifications. Now edit each of the programs again with the following
two new updates:

  1. Move the instructions that read the input outside the body of
    the `main()` function and place them right before the call to the
    `main()` function.
  2. Parametrize the `main()` function with the variables that store
    the input, i.e., writing `main(x)` if `x` were the variable that
    stores the input. At this point, verify that the program runs in
    exactly the same way as before.
  3. Replace the calls to the `print()` function, printing the result
     message, by an assignment of that result message to a variable
     called `res`. Insert the following line as last line in the body
     of the `main()` function:

      ```
      return(res)
      ```
  4. Replace the call to the function `main()` by:

      ```
      print(main(x))
      ```
   assuming that `x` is the name of the variable that stores the input.

Verify that the program runs in exactly the same way as before these
modifications. Try to understand the flow of the input information into
the code that makes the actual calculations and the flow of the output
from the `main()` function to the screen.

# How to take arguments from the command line.

Programs such as Unix commands, may take the so-called
[command-line arguments](https://en.wikipedia.org/wiki/Command-line_interface#Arguments),
which allow programs to read different input each time we run them
For instance, the `cp` file-copying command requires two arguments, the
file to copy and the target directory or file where it
should be copied, for instance:

```
$ cp ~/Download/rawData.zip .
```
[Command-line arguments](https://en.wikipedia.org/wiki/Command-line_interface#Arguments)
allow us to re-use programs with different input and enable automatizing
[workflows](https://en.wikipedia.org/wiki/Workflow). We will see in this
section how can we take command-line arguments through the code in our own
Python programs.

We can use the Python module `sys` (to refresh the concept of a Python module,
see the corresponding section in
[this lecture](https://funcompbio.github.io/lecture5/#25))
to fetch argument values given by the user in the command line. To illustrate
this functionality, create a text file called `showargs.py` and add the
following lines:

```
import sys
i = 0
while i < len(sys.argv) :
  print(f"argument vector position {i}: {sys.argv[i]}")
  i = i + 1
```

If you call this program from the Unix command line with the arguments
`give me 5`, you should be getting the following output:

```
$ python showargs.py give me 5
argument vector position 0: showargs.py
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
numbers to be evaluated; see the slides on functions from
[this lecture](https://funcompbio.github.io/lecture5/#20).
The function `main(x, y)` should return a character string
value set to `yes` when `x` and `y` are relatively prime and `no` when
they are not. This function **should not** print anything on the screen.

3. When the program is called from the command line without the two
arguments corresponding to the two positive integer values to evaluate,
then for a program called, e.g., `relprime.py`, the user should get a
message like:

    ```
    $ python relprime.py
    error: relprime.py <x> <y>
    ```

4. When the program is properly called from the command line with the two
arguments corresponding to the two positive integer values to evaluate,
then the program should call the previously defined `main(x, y)` function,
take its result and print it in the terminal screen. For instance, this
could be an example of a proper command-line call and its result.

    ```
    $ python relprime.py 4 9
    relatively primes!
    ```

