"""
Напишите программу, которая приветствует пользователя, выводя слово «Привет» (без кавычек), после которого должна стоять запятая и пробел, а затем введенное имя и восклицательный знак.

Формат входных данных
На вход программе подаётся одна строка — имя пользователя.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание 1. Перед восклицательным знаком не должно быть пробелов.

Примечание 2. Для считывания текста используйте команду input(), для печати текста на экране используйте команду print().

Примечание 3. Используйте необязательный параметр end.
"""

name = input()
print("Привет,", name, end="!")
