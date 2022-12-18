# 1) Сделать игру морской бой


import random

print("\t***Морской бой*** \n\tПравила: Компьютер спрятал корабль на клетке от 1 до 9, найди его. \n\tЦель: Уничтож его!!! ")
print('*' * 9)
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in x:
    print(i)
print('*' * 9)
a1 = random.choice(x)
a2 = random.choice(a1)
# print(a2) # Подсказка!!!!!!!!!!!!!
hit = 0
while a2 != hit:
    hit = int(input("Введите клетку: "))
    if hit != a2:
        print("Не попал")
    elif hit == a2:
        print("Попал, ты уничтожил его")
