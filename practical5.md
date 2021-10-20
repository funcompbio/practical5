---
layout: page
title: Practical 5
permalink: /practical5/
---

# Objectives

The learning objectives for this practical are:

 * Implement a program in Python that decides if two given numbers are relatively primes.
 * Implement a program in Python that decides if a given number is cool.
 * Bundling lines together into functions.
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
entitled "Debugging" from [practical 4](/practical4#debugging/).

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

# Execution modes in Python

There are three main ways in which you can run a Python program:

1. Running it from the Unix shell command line.

2. Interactively, through the Python shell interpreter.

3. Importing Python code as a so-called _module_ into another Python program.

Actually, the first two ways are equivalent and only the third one is
qualitatively different from the first two. To understand that difference we
need to learn that Python defines for us a variable called
[`__name__`](https://docs.python.org/3/library/__main__.html),
in which Python stores the name of the _scope_ in which top-level code
executes. This _scope name_ will be either the name of the module to which
the code belongs to, when running in the previously described situation (3),
or the value `__main__`, when running in one of the previously situations
described in (1) and (2).

Create a text file called `thismodule.py` and put the following line on it:

```
print("__name__: %s" %(__name__))
```

Now let's call this Python program from the Unix shell command line:

```
$ python thismodule.py 
__name__: __main__
```

We can see that when calling the Python program `thismodule.py` from the
Unix shell command line, the `__name__` variable takes the value `__main__`.
Now start the Python shell interpreter (calling `python` or `python3` from
the Unix command line without arguments), directly type the `__name__`
variable and hit the `Enter` key:

```
>>> __name__
`__main__`
```

We also see here that in the Python interactive prompt `__name__` takes the
value `__main__`. Finally, from this same prompt let's import the code in
`thismodule.py` as if we were importing it in some other Python program:

```
>>> import thismodule
__name__: thismodule
```

Differentely to the previous two execution modes, when importing Python code
as a _module_ (see the slide about modules on
[this lecture](https://funcompbio.github.io/lecture5/#15)),
the `__name__` variable takes the value of the module name, defined by the
filename containing the imported code, without the `.py` extension.

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

We have seen in the previous section that the `__name__` variable allows us
to detect in our Python code when it is executing from the Unix shell
command line. In this particular execution mode, we can use the Python
module `sys` to fetch argument values given by the user in the command line.
To illustrate this functionality, edit the previous file `thismodule.py` and
add the following lines:

```
if __name__ == "__main__" :
  import sys
  i = 0
  while i < len(sys.argv) :
    print("argument vector position %d: %s" %(i, sys.argv[i]))
    i = i + 1
```

If you call this program from the Unix command line with the arguments
`give me 5`, you should be getting the following output:

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
numbers to be evaluated; see the slides on functions from
[this lecture](https://funcompbio.github.io/lecture5/#11).
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
take its result and print it in the terminal screen.

# Reading DNA from FASTA files

Following the explanation from Wikipedia, in bioinformatics
the [**FASTA format**](https://en.wikipedia.org/wiki/FASTA_format) is a
text-based [file format](https://en.wikipedia.org/wiki/FASTA_format)
for representing sequences of either
[nucleic acids](https://en.wikipedia.org/wiki/Nucleic_acid_sequence) or
[amino acids](https://en.wikipedia.org/wiki/Amino_acid). Here, we want
to learn how can we read from a Python program the DNA sequence of a gene
stored in FASTA format within a text file and make some simple summaries
of the DNA content from that gene. We are going to illustrate
that task with the 
[_hemoglobin subunit beta_ (HBB) gene](https://en.wikipedia.org/wiki/Hemoglobin_subunit_beta), which is a gene coding for a protein that forms part of
[haemoglobin](https://en.wikipedia.org/wiki/Hemoglobin), the molecule
responsible for transporting oxygen in
[red blood cells](https://en.wikipedia.org/wiki/Red_blood_cell) of
almost all
[vertebrates](https://en.wikipedia.org/wiki/Vertebrate).

First, let's download the FASTA file of the DNA of the human _HBB_ gene
following these steps:

1. Go to the NCBI web page for the human _HBB_ gene at this
  [link](https://www.ncbi.nlm.nih.gov/gene/3043).
2. Click on `Download Datasets` and in the popup window the
  `Gene sequences (FASTA) option should be checked. Press the
  button `Download`. A ZIP file called `HBB_datasets.zip` will
  be downloaded, store it into the folder for this practical.
3. Uncompress the file `HBB_datasets.zip` and copy the file
      ```
      ncbi_dataset/data/gene.fna
      ```
   to your CWD under the name `HBB.fa`. This is the FASTA file
   containing the DNA of the human _HBB_ gene.
4. Examine the first lines of this FASTA file with the Unix
   `head` command. The result should be as follows:

      ```
      $ head HBB.fa
      >NC_000011.10:c5227071-5225464 HBB [organism=Homo sapiens] [GeneID=3043] [chromosome=11]
      ACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCATCTGACTCCTGA
      GGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGC
      AGGTTGGTATCAAGGTTACAAGACAGGTTTAAGGAGACCAATAGAAACTGGGCATGTGGAGACAGAGAAG
      ACTCTTGGGTTTCTGATAGGCACTGACTCTCTCTGCCTATTGGTCTATTTTCCCACCCTTAGGCTGCTGG
      TGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATGCTGTTATGGG
      CAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGCTCACCTGGAC
      AACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGATCCTGAGAACT
      TCAGGGTGAGTCTATGGGACGCTTGATGTTTTCTTTCCCCTTCTTTTCTATGGTTAAGTTCATGTCATAG
      GAAGGGGATAAGTAACAGGGTACAGTTTAGAATGGGAAACAGACGAATGATTGCATCAGTGTGGAAGTCT
      ```

Next, create a new text file called `tallynt.py` with the following
contents:

```
f = open("HBB.fa")
line = f.readline()                  ## read the first line from HBB.fa
print("The DNA sequence from gene:")
print(line.strip())                  ## print the first line from HBB.fa

seq = ""                             ## seq will store the whole gene DNA
while (line) :                       ## while 'line' is not empty
    line = f.readline()              ## read the next line from HBB.fa
    seq = seq + line.strip()         ## concatenate that line to 'seq'

v = list(seq)                        ## convert 'seq' into a vector 'v'
n = len(v)                           ## calculate the length of vector 'v'
print("has a total of %d nucleotides" %(n))
```

This Python program reads the lines from `HBB.fa` and concanates them
into a single character strings called `seq`, which afterwards is
converted into a vector `v` from which we calculate its length,
corresponding to the total number of nucleotides in the DNA encoding
the gene _HBB_. It includes a call to the method
[`strip()`](https://www.w3schools.com/python/ref_string_strip.asp),
which when called from a `str` object, it removes any leading and trailing
spaces and newlines. When you run this program, the output must be as follows:

```
$ python tallynt.py
The DNA sequence from gene:
>NC_000011.10:c5227071-5225464 HBB [organism=Homo sapiens] [GeneID=3043] [chromosome=11]
has a total of 1608 nucleotides
```
Now, improve this program with the following two enhancements:

1. Enable the program to take the name of the FASTA file as a first
  argument in the command line, so that it can work with any FASTA
  file containing DNA from any gene. Run it, for instance, with the
  DNA from the the
  [_ACE2_ gene](https://www.ncbi.nlm.nih.gov/gene/59272), which
  encodes a protein that acts as a receptor for the spike glycoprotein
  of the human coronavirus SARS-CoV-2, the causative agent of
  coronavirus disease-2019 (COVID-19), e.g.:
      ```
      $ python tallynt.py ACE2.fa
      ```

2. Enable the program to take a second argument where we specify one
  of the four possible nucleotides (`A`, `C`, `G` or `T`) and it
  calculates the number of occurrences of that nucleotide in the DNA
  sequence of the gene, e.g.:

      ```
      $ python tallynt.py HBB.fa A
      ```
   You can verify whether the calculation is correct by doing it also
   in Unix with the following command line:

      ```
      $ grep -v HBB HBB.fa | fold -1 | grep A | wc -l
      411
      ```
   Try to understand what is doing each bit of the previous Unix
   command-line. Could you think of a way to tally all four nucleotides
   in the same command line?
