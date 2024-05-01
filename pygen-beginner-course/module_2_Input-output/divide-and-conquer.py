"""
Divide and Conquer
Write a program that reads a positive integer x and displays a sequence of numbers x, 2x, 3x, 4x, and 5x, separated by three dashes.

Input format:
The program receives a positive integer as input.

Output format:
The program should display the text according to the task condition.
"""

a = int(input())
print(a, 2 * a, 3 * a, 4 * a, 5 * a, sep="---")
