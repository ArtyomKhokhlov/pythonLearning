"""
Write a program that calculates the cost of three computers, each consisting of a monitor, a system unit, a keyboard, and a mouse.

Input Format
The program receives four integers, each on a separate line. The first line contains the cost of the monitor, the second line the cost of the system unit, the third line the cost of the keyboard, and the fourth line the cost of the mouse.

Output Format
The program should output a single number – the total purchase cost (for three computers).
"""

monitor = int(input())
pc = int(input())
keyboard = int(input())
mouse = int(input())
print((monitor + pc + keyboard + mouse) * 3)
