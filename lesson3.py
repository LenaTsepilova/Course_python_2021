"""урок 3. задание 1"""

# def divide(arg1, arg2):
#     if arg2 == 0:
#         return "на ноль делить нельзя"
#     return arg1 / arg2
#
#
# print(divide(5, 0))

"""урок 3. задание 2"""
#
# def data(name, mail, lastname):
#     return name + " " + lastname + " " + mail
#
# input_name = input()
#
# print(data(lastname="jhdjfhdjfhdjfh", name=input_name, mail="fjhkhkhkh"))

"""урок 3. задание 3"""
#
# def two_max_number(num1, num2, num3):
#     numbers = [num1, num2, num3]
#     one_max = max(numbers)
#     numbers.pop(numbers.index(one_max))
#     two_max = max((numbers))
#     return one_max + two_max
# print(two_max_number(7, 55, 1000))

"""урок 3. задание 4"""

#
# def my_func(x, y):
#     return x ** y
#
#
# print(my_func(float(input()), int(input())))

"""урок 3. задание 5"""

total = 0


def my_func(*arg):
    global total
    numbers = arg[0]
    for i in numbers:
        if i.isdigit():
            total += int(i)
        else:
            return print("программа завершена. сумма:", total)
    return print("промежуточная сумма:", total), my_func(input("продолжите ввод, если хотите выйти введите спец-символ:\n").split())


my_func(input("введите числа через пробел:\n").split())
