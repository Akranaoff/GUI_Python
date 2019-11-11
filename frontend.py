from tkinter import *
from backend import *

def view_command():
    list1.delete(0,END)
    result = display()
    for i in result:
        list1.insert(END,i)

def search_command():
    list1.delete(0,END)
    result = search(title_text.get(),author_text.get(),isbn_text.get(),year_text.get())
    for i in result:
        list1.insert(END,i)

def delete_command():
    delete(title_text.get())

def add_command():
    insert(title_text.get(),author_text.get(),isbn_text.get(),year_text.get())
    list1.delete(0,END)
    list1.insert(END, (title_text.get(),author_text.get(),isbn_text.get(),year_text.get()))

def update_command():
    update(author_text.get(),isbn_text.get(),year_text.get(),title_text.get())
    list1.delete(0,END)
    #list1.update(END, (author_text.get(),isbn_text.get(),year_text.get(),title_text.get()))

window = Tk()
window.wm_title("BookStore")

l1 = Label(window, text = 'TITLE')
l1.grid(row=0,column=0)

l2 = Label(window , text = 'AUTHOR')
l2.grid(row = 0 , column = 2)

l3 = Label(window , text = 'YEAR')
l3.grid(row = 1, column = 0)

l4 = Label(window , text = 'ISBN')
l4.grid(row = 1, column = 2)



title_text = StringVar()
e1 = Entry(window, textvariable = title_text)
e1.grid(row = 0, column = 1)

author_text = StringVar()
e1 = Entry(window, textvariable = author_text)
e1.grid(row = 0, column = 3)

year_text = StringVar()
e1 = Entry(window, textvariable = year_text)
e1.grid(row = 1, column = 1)

isbn_text = StringVar()
e1 = Entry(window, textvariable = isbn_text)
e1.grid(row = 1, column = 3)


list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 2, column =  0, rowspan = 6, columnspan = 2)

sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2 , rowspan = 6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

b1 = Button(window, text = "VIEW ALL", width = 12 ,command = view_command)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = "SEARCH", width = 12, command = search_command)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "ADD",width = 12,  command = add_command)
b3.grid(row = 4, column = 3)

b5 = Button(window, text = "DELETE", width = 12, command = delete_command)
b5.grid(row = 5, column = 3)

b6 = Button(window, text = "UPDATE", width = 12, command = update_command)
b6.grid(row = 6, column = 3)







window.mainloop()

