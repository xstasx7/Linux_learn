# Сделать программу расписание - делаем расписание занятий\тренировок или что-то своё.
# Для хранения информации используем текстовые файлы (сохраняем, перезаписываем в них и т.д.),
# бесконечный цикл, функции и прочий функционал.
# Программа будет, как консольный бот, который будет нас спрашивать что и как нужно сделать - вывести,
# показать, перезаписать , добавить событие в определенный день недели
from pydoc import text

days = {1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье"}
place = {1: "спортзал", 2: "бассейн", 3: "стадион"}
training = {1: "штанга", 2: "велодорожка", 3: "заплыв", 4: "парилка", 5: "турник", 6: "тенис", 7: "бег по стадиону"}

print(f'{"*" * 6} -РАСПИСАНИЕ ЗАНЯТИЙ-{"*" * 6}')


def day_week():  # Выбирает день недели
    for k, v in days.items():
        print(f'#{k} - {v}')
    d = int(input(f"Введите номер дня недели: "))  # выбрать день
    if d <= 7:
        day_1 = days[d]  # Значение
        return day_1  # Вернем значение
    else:
        return "Такого дня недели нет в списке"


def place_run():  # Выбирает место
    for k, v in place.items():
        print(f'#{k} - {v}')
    p = int(input("Введите номер куда пойдем: "))  # Выбирать место
    if p <= 3:
        run = place[p]  # Значение
        return run  # Вернем значение
    else:
        return "Такого места нет в списке"


def go_train():
    for k, v in training.items():
        print(f'#{k} - {v}')
    t = int(input("Введите номер тренировки: "))
    if t <= 7:
        train = training[t]
        return train  # Вернем значение
    else:
        return "Такого тренировки нет в списке"


def main():
    to_do = int(input("Что делать с расписанием занятий:\n"
                      "\t#1 - Записать"
                      "\t#2 - Читать"
                      "\t#3 - Стереть\n"
                      "\tВыбор: "))
    if to_do == 1:
        x = 'д'
        while x == 'д':
            with open("text.txt", "a", encoding="UTF-8") as file:  # Открываем file
                a = day_week()
                b = place_run()
                c = go_train()
                print(f"Когда: {a}\tГде:{b}\tЧто:{c}")
                text1 = f"{a.ljust(15,'.')}{b.ljust(15,'.')}{c}\n"
                file.write(text1)
                x = input("Для продолжения введите 'д', иначе завершаем: ")
        return "Файл записан"
    elif to_do == 2:
        with open("text.txt", encoding='utf-8') as file:
            for line in file.readlines():
                print(line, end="")
    elif to_do == 3:
        with open("text.txt", "w", encoding="UTF-8") as file:  # Открываем file
            file.write("_")
            return "Информация удалена"


if __name__ == '__main__':
    print(main())
