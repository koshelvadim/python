from database import *
from view import *


def main():
    while True:
        num = input_num()
        if num == 1:
            name = input_name()
            write_name(name)
            print("Контакт успешно записано\n")
            print_lst()
        elif num == 2:
            char = input_char("Введите данные для поиска")
            read_found(char)
            print("Контакт(ы) успешно найден\n")
        elif num == 3:
            param = input_param()
            sort_lst(param)
            print_lst()
            print("Справочник успешно отсортирован\n")
        elif num == 4:
            char = input_char("Введите id для удаления записи")
            delete_contact(char)
            print_lst()
            print("Контакт успешно удален\n")
        elif num == 5:
            char = input_char("Введите id для редактирования записи")
            change_contact(char)
            print_lst()
            print("Контакт успешно изменен\n")
        elif num == 6:
            print_lst()
            print("База успешно выведена\n")
        elif num == 0:
            break


main()
