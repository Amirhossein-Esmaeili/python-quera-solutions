# Quera Python Problem Solutions

## Introduction

This repository contains a collection of solutions for Python problems and algorithmic scripts, storing implementation files in one place. The repository currently consists of 5 distinct Python files, one that tests the logic behind each of these different problem statements.

One script is dedicated to calculating an alternate sum by iterating through a given range, adding values using even or odd indices. In another file, the year and month of a date are extracted and separated using string slicing operations. The module compares two numbers digit by digit from right to left with tuples to see which is larger. There's also a perfect number implementation, checks if a number is perfect by adding all of its proper divisors and seeing if the condition is met. In the end, the theatre seat reservation script translates spatial coordinates via reflected rows and columns into order to assign its respective section.

The scripts focus on basic concepts in Python: user input, String Operation, if-else statement, and loops. Each solution is implemented in an abstract way, resulting in a consolidated repository of modular python code.

###  Alternating Sum

Problem: Write a program that calculates the rhythmic sequence value for time steps using two different parameters ($a$ and $b$) that alternate.

Description: This routine simulates wordless performance by incrementally stepping through a number of time within the loops. It makes careful use of conditional logic to decide even or odd intervals as appropriate in accordance with the precise rules of the problem to determine when to add or modify rhythm values, parameters, and time steps. Additionally, it prevents execution boundary errors involving time counters, handles input parameters flexibly, and calculates the total sequence score.

**Problem Link:** [View on Quera](https://quera.org/problemset/4065?tab=description)

###  Date Parts

Problem: Program that extracts the birth year and month from a combined string of them, and prints them both independently.   

Description: The program can handle continuous string inputs similarly. Using Python's standard string indexing and slicing methods, it extracts the correct character range of year and month respectively and print them independently and differently. It also takes care of proper formatting of data, takes into account the border cases such as the length and efficiently gets the job done without relying on any external date library.

**Problem Link:** [View on Quera](https://quera.org/problemset/615?tab=description)

###  Number Comparison

Problem: Write a 3-digit numbers two in reverse order comparison program (comparing ones, tens, and hundreds respectively).

Description: Using a precise right-to-left digit extraction technique, this solution check number ordering direction that is not been "Human-Friendly", It splits the numbers into individual digits with math operators or via a tuple, which permits the program to first compare the ones, then the tens, and finally the hundreds and determine the actual ordering. It is elegant and doesn't require any parsing skills or complex statements. The strategic use of logical, straightforward and well-structured conditionals paves the way for all the comparison.

**Problem Link:** [View on Quera](https://quera.org/problemset/3406?tab=description)

### Perfect Number
Problem: Check if an integer n is a perfect number. Print YES/NO.

Description: The solution uses an optimized iterative loop to go through factors up to n, find all proper divisors of the number, and efficiently sum these divisors without storing each of them individually. The final sum of divisors is compared to the original integer and the appropriate result is output. The script runs each mathematical test in order to guarantee its result is accurate, and creates a clean format for outputting the results.

**Problem Link:** [View on Quera](https://quera.org/problemset/282?tab=description)

### Theatre Square Seats
Problem: A program to calculate the number of rows one must move-up/down and the seat direction from the reflected (mirrored) coordinates.

Description: Using complex mathematics transformations and geometry, it maps the current coordinates to the actual physical locations. relative differences between reflected rows and mirrored columns, and accordingly it finds the coordinates of the starting point of the passenger and the target coordinates into the relative steps, row shift and final target coordinate. with all the grid layout rules of numbering, padding, and space mapping.

**Problem Link:** [View on Quera](https://quera.org/problemset/10325?tab=descriptionn)
 