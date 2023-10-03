import file_operation
import notebook
import ui

number = 5  # сколько знаков МИНИМУМ может быть в тексте заметки

def add():
    note = ui.create_note(number)
    array = file_operation.read_file()
    for notes in array:
        if notebook.Note.get_id(note) == notebook.Note.get_id(notes):
            notebook.Note.set_id(note)
    array.append(note)
    file_operation.write_file(array, 'a')
    print('Заметка добавлена...')


def show(text):
    logic = True
    array = file_operation.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(notebook.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + notebook.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in notebook.Note.get_date(notes):
                print(notebook.Note.map_note(notes))
    if logic == True:
        print('Нет ни одной заметки...')


def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: ')
    array = file_operation.read_file()
    logic = True
    for notes in array:
        if id == notebook.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = ui.create_note(number)
                notebook.Note.set_title(notes, note.get_title())
                notebook.Note.set_body(notes, note.get_body())
                notebook.Note.set_date(notes)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...')
            if text == 'show':
                print(notebook.Note.map_note(notes))
    if logic == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    file_operation.write_file(array, 'a')