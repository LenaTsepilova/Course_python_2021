"""Урок 4. Задание 1"""

# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

# import sys
# production_in_hour = int(sys.argv[1])
# payment_in_hour = int(sys.argv[2])
# bonus = int(sys.argv[3])
#
#
# def sallery(production_in_hour, payment_in_hour, bonus):
#     return production_in_hour * payment_in_hour + bonus
#
# print(sallery(production_in_hour, payment_in_hour, bonus))

"""Урок 4. Задание 2"""

# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

# my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# new_my_list = [my_list[element] for element in range(1, len(my_list)) if my_list[element] > my_list[element - 1]]
# print(new_my_list)