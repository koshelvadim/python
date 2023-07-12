def input_num():
    ask = int(
        input("Выбери действие:\n1 - записать нового контакта\n2 - поиск контакта\n3 - сортировка базы данных\n4 - удалить контакт\n5 - редактировать контакт\n6 - вывести весь справочник\n0 - выход из программы\n"))
    return ask


def input_name():
    id = input("введите id: ")
    first_name = input("введите имя: ")
    tel = input("введите телефон: ")
    res = id + "," + first_name + "," + tel + '\n'
    return res


def input_char(message):
    char = input(f"{message}: ")
    return char


def input_param():
    param = input(
        "Выбери действие сортировки:\n1 - по идентификатору\n2 - по ФИО\n3 - по номеру телефона\n")
    if param == '1' or param == '2' or param == '3':
        return int(param) - 1
    else:
        print("такая сортировка не предусмотрена\n")
        input_param()


