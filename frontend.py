"""
Программа для хранения информации о книгах: автор, название, год издания, ISBN.
Пользователь может: посмотреть данные, внести данные, удалить данные, искать конкретные данные.
"""
import backend
from tkinter import *


def get_selected_row(event):
    try:
        global selected_tuple
        index = listbox_1.curselection()[0]
        selected_tuple = listbox_1.get(index)
        entry_1.delete(0, END)
        entry_1.insert(END, selected_tuple[1])
        entry_2.delete(0, END)
        entry_2.insert(END, selected_tuple[2])
        entry_3.delete(0, END)
        entry_3.insert(END, selected_tuple[3])
        entry_4.delete(0, END)
        entry_4.insert(END, selected_tuple[4])
        entry_5.delete(0, END)
        entry_5.insert(END, selected_tuple[5])
        entry_6.delete(0, END)
        entry_6.insert(END, selected_tuple[6])
    except IndexError:
        pass


def view_command():
    listbox_1.delete(0, END)
    for row in backend.view():
        listbox_1.insert(END, row)


def search_command():
    listbox_1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), genre_text.get(),
                              year_text.get(), isbn_text.get(), mark_text.get()):
        listbox_1.insert(END, row)


def add_command():
    backend.insert(title_text.get(), author_text.get(), genre_text.get(),
                   year_text.get(), isbn_text.get(), mark_text.get())
    listbox_1.delete(0, END)
    listbox_1.insert(END, (title_text.get(), author_text.get(), genre_text.get(),
                   year_text.get(), isbn_text.get(), mark_text.get()))


def delete_command():
    backend.delete(selected_tuple[0])


def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), genre_text.get(),
                   year_text.get(), isbn_text.get(), mark_text.get())


window = Tk()
window.geometry("560x220")
window.wm_title("Домашняя библиотека")

label_1 = Label(window, text="Название")
label_1.grid(row=0, column=0)

label_2 = Label(window, text="Автор")
label_2.grid(row=0, column=2)

label_3 = Label(window, text="Жанр")
label_3.grid(row=0, column=4)

label_4 = Label(window, text="Год издания")
label_4.grid(row=1, column=0)

label_5 = Label(window, text="ISBN")
label_5.grid(row=1, column=2)

label_6 = Label(window, text="Оценка")
label_6.grid(row=1, column=4)

title_text = StringVar()
entry_1 = Entry(window, textvariable=title_text)
entry_1.grid(row=0, column=1)

author_text = StringVar()
entry_2 = Entry(window, textvariable=author_text)
entry_2.grid(row=0, column=3)

genre_text = StringVar()
entry_3 = Entry(window, textvariable=genre_text)
entry_3.grid(row=0, column=5)

year_text = StringVar()
entry_4 = Entry(window, textvariable=year_text)
entry_4.grid(row=1, column=1)

isbn_text = StringVar()
entry_5 = Entry(window, textvariable=isbn_text)
entry_5.grid(row=1, column=3)

mark_text = StringVar()
entry_6 = Entry(window, textvariable=mark_text)
entry_6.grid(row=1, column=5)

listbox_1 = Listbox(window, height=9, width=55)
listbox_1.grid(row=3, column=0, rowspan=8, columnspan=5)

scrollbar_1 = Scrollbar(window)
scrollbar_1.grid(row=2, column=4, rowspan=8)

listbox_1.configure(yscrollcommand=scrollbar_1.set)
scrollbar_1.configure(command=listbox_1.yview)

listbox_1.bind("<<ListboxSelect>>", get_selected_row)

button_1 = Button(window, text="Показать всё", width=12, command=view_command)
button_1.grid(row=4, column=5)

button_2 = Button(window, text="Поиск", width=12, command=search_command)
button_2.grid(row=5, column=5)

button_3 = Button(window, text="Добавить", width=12, command=add_command)
button_3.grid(row=6, column=5)

button_4 = Button(window, text="Обновить", width=12, command=update_command)
button_4.grid(row=7, column=5)

button_5 = Button(window, text="Удалить", width=12, command=delete_command)
button_5.grid(row=8, column=5)

button_6 = Button(window, text="Закрыть", width=12, command=window.destroy)
button_6.grid(row=9, column=5)

window.mainloop()