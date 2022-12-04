# 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
#
# week = int(input("Введите выходной день недели цифрой: "))
# if week >= 1 and week <= 5:
#     print(f' - {week} -> нет')
# elif week < 1 or week > 7:
#     print(f' - {week} -> это ошибка, в неделе семь дней')
# else:
#     print(f' - {week} -> да')

#####################################################################################

#1. Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print(not (x or y or z) == (not x and not y and not z))
#             print(x, y, z)

#####################################################################################

# 2. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# coordinate_x = int(input("Введите координату X: "))
# coordinate_y = int(input("Введите координату Y: "))
#
# if coordinate_x == 0 and coordinate_y == 0:
#     print(f"X ≠ 0 и Y ≠ 0")
# elif coordinate_x >= 1 and coordinate_y >= 1:
#     print(f"x={coordinate_x}; y={coordinate_y} -> 1")
# elif coordinate_x <= 1 and coordinate_y >= 1:
#     print(f"x={coordinate_x}; y={coordinate_y} -> 2")
# elif coordinate_x <= 1 and coordinate_y <= 1:
#     print(f"x={coordinate_x}; y={coordinate_y} -> 3")
# elif coordinate_x >= 1 and coordinate_y <= 1:
#     print(f"x={coordinate_x}; y={coordinate_y} -> 4")
# else:
#     print(f"Читай условие")

#####################################################################################

# 1. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
#
# num_quarter = int(input("Введите номер четверти: "))
#
# if num_quarter == 1:
#     print(f"x >= 1 and y >= 1")
# elif num_quarter == 2:
#     print(f"x <= 1 and y >= 1")
# elif num_quarter == 3:
#     print(f"x <= 1 and y <= 1")
# elif num_quarter == 4:
#     print(f"x >= 1 and y <= 1")
# else:
#     print(f"Читай условие")

#####################################################################################

#2. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# print("Введите координаты точки А: ")
# x_a = int(input('X: '))
# y_a = int(input('Y: '))
# print("Введите координаты точки B: ")
# x_b = int(input('X: '))
# y_b = int(input('Y: '))
# num = ((x_a - x_b) ** 2 + (y_a - y_b) ** 2)
# dist = round(num ** 0.5, 2)
# print(f'A ({x_a},{y_a}; B ({x_b},{y_b}) -> {dist}')
