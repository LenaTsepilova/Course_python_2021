
"""Урок 1. Задание 2"""
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

# n = int(input("введите время в секундах: \n"))
# # print(1, 2, 3, sep=":")
# # print(str(n // 3600) + ":" + str(n % 3600 // 60) + ":" + str(n % 60))
# h = n // 3600
# m = n % 3600 // 60
# s = n % 60
# print('{:02d}:{:02d}:{:02d}'.format(h, m, s))

"""Урок 1. Задание 3"""

# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

# n = input("введите целое число:")
# print(int(n) + int(n * 2) + int(n * 3))

"""Урок 1. Задание 4"""

# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

# n = int(input("введите число: "))
# max_number = 0
# while n > 0:
#     if n % 10 > max_number:
#         max_number = n % 10
#     n = n // 10
# print(max_number)

"""Урок 1. Задание 5"""
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или
# убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников
# фирмы и определите прибыль фирмы в расчете на одного сотрудника.

# v = int(input("введите выручку:"))
# i = int(input("введите издержки:"))

# if v > i:
#     print("прибыль")
#     r = (v - i) / v
#     print("Рентабельность равна:", r)
#     p = int(input("введите количество сотрудников: "))
#     print((v - i) / p, "прибыль фирмы в расчете на одного сотрудника")
# else:
#     print("убыток")
