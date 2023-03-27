from tkinter import *
from tkinter import ttk


# root.screen(700, 200)

# while True:
#     students = [(5540433388, 'readed joke 1-9', '2023-03-25 11:39:51'), (5540433388, 'readed joke 10-19', '2023-03-25 11:39:58'), (5540433388, 'calculate', '2023-03-25 11:40:21'), (5540433388, 'wanted word', '2023-03-25 11:40:59'), (5540433388, 'played rsph', '2023-03-25 11:41:16')]

#     columns = ['name', 'age', 'email']

#     tree = ttk.Treeview(columns=columns)
#     tree.pack(fill=BOTH, expand=1)

#     tree.heading('name', text="Имя")
#     tree.heading('name', text="Возвраст")
#     tree.heading('name', text="Почта")

#     for student in students:
#         tree.insert("", END, values=student)
#     root.mainloop()
#     print(1)


# root.mainloop()

root = Tk()
root.title("Telegram Bot")
students = [(5540433388, 'readed joke 1-9', '2023-03-25 11:39:51'), (5540433388, 'readed joke 10-19', '2023-03-25 11:39:58'), (5540433388, 'calculate', '2023-03-25 11:40:21'), (5540433388, 'wanted word', '2023-03-25 11:40:59'), (5540433388, 'played rsph', '2023-03-25 11:41:16')]
columns = ['name', 'age', 'email']

tree = ttk.Treeview(columns=columns)
tree.pack(fill=BOTH, expand=1)

tree.heading('name', text="Имя")
tree.heading('name', text="Возвраст")
tree.heading('name', text="Почта")

for student in students:
    tree.insert("", END, values=student)




def button_func():
    # root.destroy()
    # root = Tk()
    # root.title("Telegram Bot")

    # students = [(5540433388, 'readed joke 1-9', '2023-03-25 11:39:51'), (5540433388, 'readed joke 10-19', '2023-03-25 11:39:58'), (5540433388, 'calculate', '2023-03-25 11:40:21'), (5540433388, 'wanted word', '2023-03-25 11:40:59'), (5540433388, 'played rsph', '2023-03-25 11:41:16')]

    # columns = ['name', 'age', 'email']

    # tree = ttk.Treeview(columns=columns)
    # tree.pack(fill=BOTH, expand=1)

    # tree.heading('name', text="Имя")
    # tree.heading('name', text="Возвраст")
    # tree.heading('name', text="Почта")

    # for student in students:
    #     tree.insert("", END, values=student)

    # root.mainloop()
    root.update()

b = Entry(root)
b.pack()
button_ = Button(root, text='Reload page', command=button_func)
button_.pack()

a = tuple(input("What to append?: "))
students.append(a)
root.mainloop()

# from tkinter import *

# def blink():
#     e.config(bg='green')
#     e.after(1000, lambda: e.config(bg='white')) # after 1000ms

# root = Tk()
# e = Entry(root)
# e.pack()
# b = Button(root, text='blink', command=blink)
# b.pack()
# root.mainloop()
