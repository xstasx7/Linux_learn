# 1) Вводим с клавиатуры целое число X и У.
# Выводим на экран количество чисел между Х и У, которые делятся на 2 и 3

# num_x = int(input("Введите целое число x: "))
# num_y = int(input("Введите целое число y: "))
# count_2 = []
# count_3 = []
# for i in range(num_x, num_y):
#     if i % 2 == 0:
#         count_2.append(i)
# for i in range(num_x, num_y):
#     if i % 3 == 0:
#         count_3.append(i)
# print(f'Количество чисел которые делятся на два в диапозоне x-y -> {len(count_2)}')
# print(f'Количество чисел которые делятся на три в диапозоне x-y -> {len(count_3)}')

#######################################################################################

# 2) Вводим с клавиатуры целое число X
# Далее вводим Х целых чисел.
# Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.
#
# num_x = []
# num_max = int(input('Введите целое число X: '))
# num_x.append(num_max)
# while num_max != 0:
#     num_max = int(input('Вводите целые числа, если достаточно введите "0": '))
#     num_x.append(num_max)
# print(f"Вот получился список:\n{num_x}")
# max_one = num_x[0]
# for i in num_x:
#     if i > max_one:
#         max_one = i
# num_x.remove(max_one)
# max_two = num_x[0]
# for i in num_x:
#     if i > max_two:
#         max_two = i
# print(f"Это два максимальных числа из списка: {max_one}, {max_two}")

#######################################################################################

# 3) Вводим с клавиатуры целое число - это зарплата.
# Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
# И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых
#
# salary = []
# count_25 = []
# count_10 = []
# count_3 = []
# count_1 = []
# while salary != 0:
#     salary = int(input("Введите зарплату: "))
#     if salary >= 25:
#         for i in range(1, salary+1):
#             if i % 25 == 0:
#                 count_25.append(i)
#         salary -= count_25[-1]
#     if salary >= 10 and salary < 25:
#         for i in range(1, salary + 1):
#             if i % 10 == 0:
#                 count_10.append(i)
#         salary -= count_10[-1]
#     if salary >= 3 and salary < 10:
#         for i in range(1, salary + 1):
#             if i % 3 == 0:
#                 count_3.append(i)
#         salary -= count_3[-1]
#     if salary > 0 and salary <= 2:
#         for i in range(1, salary + 1):
#             if i % 1 == 0:
#                 count_1.append(i)
#         salary -= count_1[-1]
# print(f"Минимальное количество купюр: {len(count_25 + count_10 + count_3 + count_1)}")
# print(f"Из них\n"
#       f"25 рублевые: {len(count_25)}\n"
#       f"10 рублевые: {len(count_10)}\n"
#       f"3 рублевые:  {len(count_3)}\n"
#       f"1 рублевые:  {len(count_1)}\n ")

#######################################################################################

# 4) Вводим с клавиатуры многозначное число
# Необходимо узнать и сказать последовательность цифр этого числа
# при просмотре слева направо упорядочена по возрастанию или нет.
# Например 1579 - да ( 1 меньше 5, 5 меньше 7, а 7 меньше 9), 1427 - нет
#
# number = int(input("Ввести многозначное число: "))
# num_list = []
# for i in str(number):
#     num_list.append(i)
# for x in range(len(num_list)):
#     if num_list[x] > num_list[x - 1]:
#         x += 1
#         answer = "да"
#     elif x == 0:
#         continue
#     else:
#         answer = "нет"
#         break
# print("Упорядочено по возрастанию:\n"
#       "{} - {}".format(number, answer))
