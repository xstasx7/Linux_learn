# 1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
#
# def sum_num(a): # Функция для суммирования нечетных чисел из списка
#     sum_odd = 0
#     for i in a()[1::2]:
#         sum_odd = int(i) + sum_odd
#     return f'{"-" * 36} \n Сумма нечётных элементов списка: {sum_odd}'
#
#
# def num_list(): # Функция для создания списка из набора чисел
#     list_num = []
#     list_insert = []
#     while list_insert != 'д':
#         list_insert = input("Запишите числа в список и нажмите 'д': ")
#         if list_insert == 'д':
#             break
#         list_num.append(list_insert)
#     return list_num
#
#
# if __name__ == '__main__':
#     print(sum_num(num_list))

##############################################################################

# 2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
    # И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)
# import random
# a = []
# b = []
# c = []
#
# for i in range(3): # генерируем массив А
#     a_ran = random.randint(1, 10)
#     a.append(a_ran)
# c.append(a)
# for x in range(3): # генерируем массив В
#     b_ran = random.randint(1, 10)
#     b.append(b_ran)
# c.append(b)
#
# print(c)
# # Средне арифметическое А
# count = 0
# sum_1 = 0
# for s in a:
#     sum_1 += s
#     s+=1
# # Средне арифметическое B
# count = 0
# sum_2 = 0
# for s in b:
#     sum_2 += s
#     s+=1
# print(f'{sum_1 / 3:.2f} {sum_2 / 3:.2f}')

##############################################################################

# 3) Сгенерируйте  список на 30 элементов.
# Отсортируйте список по возрастанию, методом сортировки выбором.

# import random
# # Генерирует  список на 30 элементов
# gen_list = [] # Наполняем список
# for _ in range(30): # 30 итераций
#     _ = random.randint(1, 100) # диапозон рандомного числа от 1 до 100
#     gen_list.append(_) # Добавляем в список рандомное число
# print(gen_list) # Список из 30 рандомных элементов

# Методом сортировки выбором
# num_list = len(gen_list)      # число элементов в списке
# for i in range(num_list-1):   # итерация на -1 от j
#     min_num = gen_list[i]           # запоминаем минимальное значение
#     index_min_num = i               # запоминаем индекс минимального значения
#     for j in range(i+1, num_list):  # итерация на +1 от i
#         if min_num > gen_list[j]:  # поиск миимального среди оставшихся элементов
#             min_num = gen_list[j]
#             index_min_num = j
#
#     if index_min_num != i:          # меняем, если был найден минимальный не в i-й позиции
#         temp_val = gen_list[i]
#         gen_list[i] = gen_list[index_min_num]
#         gen_list[index_min_num] = temp_val
#         # gen_list[i], gen_list[index_min_num] = gen_list[i], gen_list[index_min_num]
#
#
# print(gen_list)

