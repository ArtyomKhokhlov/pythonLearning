"""
Напишите программу, которая считывает строку-разделитель и три строки, а затем выводит указанные строки через разделитель.

Формат входных данных
На вход программе подаётся строка-разделитель и три строки, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести введённые три строки через разделитель.

Примечание 1. Для считывания текста используйте команду input(), для печати текста на экране используйте команду print().

Примечание 2. Используйте необязательный параметр sep.
"""

sep = input()
first_string = input()
second_string = input()
third_string = input()
print(first_string, second_string, third_string, sep=sep)
