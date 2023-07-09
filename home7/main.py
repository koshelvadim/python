def enterTask():
    str = int(input("Enter number of task (34 or 36 or 0 to exit): "))
    if str == 34:
        task34()
    elif str == 36:
        task36()
    elif str == 0:
        return
    else:
        print("It is wrong number!")
        enterTask()
    print("\n")
    enterTask()
# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод:
# Парам пам-пам


def task34():
    print("start task34")
    string = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

    def rhythm(string):
        string = string.split()
        list_1 = []
        for word in string:
            sum_w = 0
            for i in word:
                if i in 'аеёиоуыэюя':
                    sum_w += 1
            list_1.append(sum_w)
            print(list_1)
        return len(list_1) == list_1.count(list_1[0])

    if rhythm(string):
        print('Парам пам-пам')
    else:
        print('Пам парам')
    print("end task34")


# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения
# Ввод: print_operation_table(lambda x, y: x * y)
# Вывод:
#  1 2 3 4 5 6
#  2 4 6 8 10 12
#  3 6 9 12 15 18
#  4 8 12 16 20 24
#  5 10 15 20 25 30
#  6 12 18 24 30 36

def task36():
    print("start task36")

    def print_operation_table(operation, num_rows, num_columns):
        for i in range(1, num_rows + 1):
            print()
            for j in range(1, num_columns + 1):
                print(operation(i, j), end=" ")

    print_operation_table(lambda x, y: x * y, 6, 6)
    print()
    print("end task36")


enterTask()
