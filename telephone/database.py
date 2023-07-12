from view import *

def write_name(name):
    with open("tel.txt", "a", encoding="UTF-8") as file:
        file.write(name)


def read_found(char):
    with open("tel.txt", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        count = 1
        for row in lst:
            if char in row:
                print(f"{count} id-{row.split(',')[0]}, ФИО-{row.split(',')[1]}, тел.-{row.split(',')[2]}")
                count += 1


def sort_lst(param):
    with open("tel.txt", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        lst.sort(key=lambda x: x.split(",")[int(param)])
    with open("tel.txt", "w", encoding="UTF-8") as file:
        for row in lst:
            file.write(row)


def print_lst():
    with open("tel.txt", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        count = 1
        for row in lst:
            print(f"{count} id-{row.split(',')[0]}, ФИО-{row.split(',')[1]}, тел.-{row.split(',')[2]}")
            count += 1


def delete_contact(char):
    with open("tel.txt", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        for row in lst:
            if char in row[0]:
                lst.remove(row)
                with open("tel.txt", "w", encoding="UTF-8") as file:
                    for row in lst:
                        file.write(row)


def change_contact(char):
    with open("tel.txt", "r", encoding="UTF-8") as file:
        lst = file.readlines()
        for row in lst:
            if char in row[0]:
                lst.remove(row)
                name = input_name()
                lst.append(name)
                with open("tel.txt", "w", encoding="UTF-8") as file:
                    for row in lst:
                        file.write(row)