import cmath
from tkinter import *
from tkinter.ttk import Treeview
import random
import numpy as np
from PIL import ImageTk, Image
from math import *

root = Tk()
root.title("Лабораторные работы по ИСРПО Улитиной К.В.")
root.geometry("500x400")
root.configure(bg="beige")

#создание окна лабы 1
def createWindowLab_1():

    def show_answer():
        try:
            b = float(entry.get())  # получаем введенный текст, entry- поле
            if b == -2:
                label_one["text"] = "Уравнение не имеет решения, введите другое значение переменной b"
            elif b<2:
                z1 = (cmath.sqrt(2 * b + cmath.sqrt(b * b - 4))) / ((cmath.sqrt(b * b - 4)) + b + 2)
                z2 = 1 / (cmath.sqrt(b + 2))
                label_one["text"] = "z1 = " + str(z1)
                label_two["text"] = "z2 = " + str(z2)
            else:
                z1 = (sqrt(2 * b + sqrt(b * b - 4))) / ((sqrt(b * b - 4)) + b + 2)
                z2 = 1 / (sqrt(b + 2))
                label_one["text"] = "z1 = " + str(z1)
                label_two["text"] = "z2 = " + str(z2)
        except:
            label_one["text"] = "Некорректный ввод"

    lab_1 = Toplevel()
    lab_1.title("Лабораторная работа 1")
    lab_1.geometry("500x450")
    lab_1.configure(bg="beige")
    lab_1.resizable(width=False, height=False)  # нельзя менять размер ячеек

    #создание фрейма
    fr_lab1 = Frame(lab_1, background="beige")
    quest = Label(lab_1, text="Лабораторная работа 1 \n Разработать приложение для вычисления значений z1 и z2. ", bg="beige")
    quest.pack(expand=True)

    #вывод изображения
    pil_image = Image.open("assets/Lab1_z1.jpg")
    fr_lab1.image = ImageTk.PhotoImage(pil_image)
    image_sprite = Label(fr_lab1, image=fr_lab1.image, bg="beige")
    image_sprite.pack(anchor=NW)

    pil_image1 = Image.open("assets/Lab1_z2.jpg")
    fr_lab1.image1 = ImageTk.PhotoImage(pil_image1)
    image_sprite1 = Label(fr_lab1, image=fr_lab1.image1, bg="beige")
    image_sprite1.pack(anchor=NW, pady=6)

    #кнопка,текстовое полe и вывод результата
    entry = Entry(fr_lab1, bg="beige")
    entry.pack(padx=6, pady=6)

    btn = Button(fr_lab1, text="Запустить", command=show_answer, bg="beige")
    btn.pack(padx=6, pady=6)

    label_one = Label(fr_lab1, bg="beige")
    label_one.pack(padx=6, pady=6)

    label_two =Label(fr_lab1, bg="beige")
    label_two.pack(padx=7, pady=7)

    fr_lab1.pack()

def createWindowLab_2():
    def remove_text():
        label_one.config(text="")
    def show_answer():
        remove_text()
        try:
            x = float(entry.get())  # получаем введенный текст, entry- поле
            if x <= -6:
                y = 1
                label_one["text"] = str(y)
            elif -6 < x <= -4:
                y = - 0.5 * x - 2
                label_one["text"] = str(y)
            elif -4 < x <= 0:
                y = sqrt(4 - pow(x + 2, 2))
                label_one["text"] = str(y)
            elif 0 < x <= 2:
                y = - sqrt(1 - pow(x - 1, 2))
                if x == 2:
                    y = 0.0
                label_one["text"] = str(y)
            elif x > 2:
                y = - x + 2
                label_one["text"] = str(y)
        except:
            label_one["text"] = "Некорректный ввод"

    lab_2 = Toplevel()
    lab_2.title("Лабораторная работа 2")
    lab_2.geometry("500x450")
    lab_2.configure(bg="beige")
    lab_2.resizable(width=False, height=False)  # нельзя менять размер ячеек

    #создание фрейма
    fr_lab2 = Frame(lab_2, background="beige")
    quest = Label(lab_2, text="Лабораторная работа 2 \n Разработать приложение для вычисления значения функции y=f(x). ", bg="beige")
    quest.pack(expand=True)

    #вывод изображения
    img = Image.open("assets/Lab2_graf.png")
    pil_image = img.resize((400, 200))
    fr_lab2.image = ImageTk.PhotoImage(pil_image)
    image_sprite = Label(fr_lab2, image=fr_lab2.image, bg="beige")
    image_sprite.pack(anchor=NW)

    #кнопка,текстовое полe и вывод результата
    entry = Entry(fr_lab2, bg="beige")
    entry.pack(padx=6, pady=6)

    btn = Button(fr_lab2, text="Запустить", command=show_answer, bg="beige")
    btn.pack(padx=6, pady=6)

    label_one = Label(fr_lab2, bg="beige")
    label_one.pack(padx=6, pady=6)

    fr_lab2.pack()

def createWindowLab_3():
    def remove_text():
        label_one.config(text="")
        label_two.config(text="")
    def show_answer():
        remove_text()
        try:
            x = int(entry_x.get())
            y = int(entry_y.get())# получаем введенный текст, entry- поле
            r = int(entry_r.get())
            a = pow(x+r, 2)+pow(y-r, 2) - pow(r, 2)
            if (x*x + y*y <= r*r and x >= 0 and y <= 0) or ((pow((-r)-x, 2) + pow(r-y, 2)) > r*r and x <= 0 and y >= 0):
                label_one["text"] = "Входит"
            else:
                label_one["text"] = "Не входит"
        except:


            label_one["text"] = "Некорректный ввод"

    lab_3 = Toplevel()
    lab_3.title("Лабораторная работа 3")
    lab_3.geometry("500x500")
    lab_3.configure(bg="beige")
    lab_3.resizable(width=False, height=False)  # нельзя менять размер ячеек

    #создание фрейма
    fr_lab3 = Frame(lab_3, background="beige")
    quest = Label(lab_3, text="Лабораторная работа 3 \n Разработать приложение для проверки \n принадлежности точки к некоторой области на плоскости. ", bg="beige")
    quest.pack(expand=True)

    #вывод изображения
    img = Image.open("assets/Lab3_graf.png")
    pil_image = img.resize((200, 200))
    fr_lab3.image = ImageTk.PhotoImage(pil_image)
    image_sprite = Label(fr_lab3, image=fr_lab3.image, bg="beige")
    image_sprite.pack(anchor=NW)


    #кнопка,текстовое полe и вывод результата
    label_x = Label(fr_lab3, text="Введите X", bg="beige")
    label_x.pack()

    entry_x = Entry(fr_lab3, bg="beige")
    entry_x.pack(padx=6, pady=6)

    label_y = Label(fr_lab3, text="Введите Y", bg="beige")
    label_y.pack()

    entry_y = Entry(fr_lab3, bg="beige")
    entry_y.pack(padx=6, pady=6)

    label_r = Label(fr_lab3, text="Введите R", bg="beige")
    label_r.pack()

    entry_r = Entry(fr_lab3, bg="beige")
    entry_r.pack(padx=6, pady=6)

    btn = Button(fr_lab3, text="Запустить", command=show_answer, bg="beige")
    btn.pack(padx=6, pady=6)

    label_one = Label(fr_lab3, bg="beige")
    label_one.pack(padx=6, pady=6)

    label_two =Label(fr_lab3, bg="beige")
    label_two.pack(padx=7, pady=7)

    fr_lab3.pack()

def createWindowLab_4():
    def remove_text():
        label_one.config(text="")

    def show_answer():
        remove_text()
        try:
            data = []
            a = int(entry_a.get())
            b = int(entry_b.get())  # получаем введенный текст, entry- поле
            n = int(entry_n.get())

            k = (b - a) / n
            m = 0
            for i in np.arange(b, a - 0.5, -k):
                m += 1
                if i <= -6:
                    x = i
                    y = 1
                    ab = (m, x, y)
                    data.append(ab)

                elif -6 < i <= -4:
                    x = i
                    y = - 0.5 * x - 2
                    ab = (m, x, y)
                    data.append(ab)

                elif -4 < i <= 0:
                    x = i
                    y = sqrt(4 - pow(x + 2, 2))
                    ab = (m, x, y)
                    data.append(ab)

                elif 0 < i <= 2:
                    x = i
                    y = - sqrt(1 - pow(x - 1, 2))
                    ab = (m, x, y)
                    data.append(ab)

                elif i > 2:

                    x = i
                    y = - x + 2
                    ab = (m, x, y)
                    data.append(ab)

            # определяем столбцы
            columns = ("n", "x", "y")


            tree = Treeview(fr_lab4, columns=columns, show="headings")
            tree.pack(side = 'left')


            # определяем заголовки
            tree.heading("n", text="N")
            tree.heading("x", text="X")
            tree.heading("y", text="Y")

            tree.column("#1", width=70)
            tree.column("#2", width=70)
            tree.column("#3", width=70)

            # добавляем данные
            for i in data:
                tree.insert(parent = '',index = 'end', values =i)


        except:

            label_one["text"] = "Некорректный ввод"

    lab_4 = Toplevel()
    lab_4.title("Лабораторная работа 4")
    lab_4.geometry("500x500")
    lab_4.configure(bg="beige")
    lab_4.resizable(width=False, height=False)  # нельзя менять размер ячеек

    # создание фрейма
    fr_lab4 = Frame(lab_4, background="beige")
    quest = Label(lab_4,
                  text="Лабораторная работа 4 \n "
                       "Разработать приложение для вывода значений функции y = f(x) в точках, \n "
                       " полученных делением отрезка [a,b] на N равных частей ",
                  bg="beige")
    quest.pack()

    # вывод изображения
    img = Image.open("assets/Lab2_graf.png")
    pil_image = img.resize((200, 100))
    fr_lab4.image = ImageTk.PhotoImage(pil_image)
    image_sprite = Label(fr_lab4, image=fr_lab4.image, bg="beige")
    image_sprite.pack(anchor=NW)

    # кнопка,текстовое полe и вывод результата
    label_n = Label(fr_lab4, text="Введите N", bg="beige")
    label_n.pack()

    entry_n = Entry(fr_lab4, bg="beige")
    entry_n.pack(padx=6, pady=6)

    label_a = Label(fr_lab4, text="Введите a", bg="beige")
    label_a.pack()

    entry_a = Entry(fr_lab4, bg="beige")
    entry_a.pack(padx=6, pady=6)

    label_b = Label(fr_lab4, text="Введите b", bg="beige")
    label_b.pack()

    entry_b = Entry(fr_lab4, bg="beige")
    entry_b.pack(padx=6, pady=6)

    btn = Button(fr_lab4, text="Запустить", command=show_answer, bg="beige")
    btn.pack(padx=6, pady=6)

    label_one = Label(fr_lab4, bg="beige")
    label_one.pack()



    fr_lab4.pack()

def createWindowLab_5():
    def remove_text():
        label_one.config(text="")
        label_two.config(text="")
    def show_answer():
        remove_text()
        try:
            r = int(entry_r.get())
            count = int(entry_count.get())# получаем введенный текст, entry- поле
            true_count = 0
            false_count = 0
            for i in range(0, count):
                x = random.uniform(-r, r)
                y = random.uniform(-r, r)
                a = pow(x + r, 2) + pow(y - r, 2) - pow(r, 2)
                if (x * x + y * y <= r * r and x >= 0 and y <= 0) or (
                        (pow((-r) - x, 2) + pow(r - y, 2)) > r * r and x <= 0 and y >= 0):
                    true_count +=1
                else:
                    false_count += 1
            label_one["text"] = "Вы полпали: " + str(true_count)
            label_two["text"] = "Вы промазали: " + str(false_count)
        except:
            label_one["text"] = "Некорректный ввод"

    lab_5 = Toplevel()
    lab_5.title("Лабораторная работа 5")
    lab_5.geometry("500x500")
    lab_5.configure(bg="beige")
    lab_5.resizable(width=False, height=False)  # нельзя менять размер ячеек

    #создание фрейма
    fr_lab5 = Frame(lab_5, background="beige")
    quest = Label(lab_5, text="Лабораторная работа 5 \n Разработать приложение для имитации \n серии выстрелов по мишени. ", bg="beige")
    quest.pack(expand=True)

    #вывод изображения
    img = Image.open("assets/Lab5.jpg")
    pil_image = img.resize((200, 200))
    fr_lab5.image = ImageTk.PhotoImage(pil_image)
    image_sprite = Label(fr_lab5, image=fr_lab5.image, bg="beige")
    image_sprite.pack(anchor=NW)

    #кнопка,текстовое полe и вывод результата
    label_r = Label(fr_lab5, text="Введите R", bg="beige")
    label_r.pack()

    entry_r = Entry(fr_lab5, bg="beige")
    entry_r.pack(padx=6, pady=6)

    label_count = Label(fr_lab5, text="Введите количество выстрелов", bg="beige")
    label_count.pack()

    entry_count = Entry(fr_lab5, bg="beige")
    entry_count.pack(padx=6, pady=6)

    btn = Button(fr_lab5, text="Запустить", command=show_answer, bg="beige")
    btn.pack(padx=6, pady=6)

    label_one = Label(fr_lab5, bg="beige")
    label_one.pack(padx=6, pady=6)

    label_two =Label(fr_lab5, bg="beige")
    label_two.pack(padx=7, pady=7)

    fr_lab5.pack()

def createWindowLab_6():
    def remove_text():
        label_one.config(text="")
        label_two.config(text="")
    def show_answer():
        remove_text()
        try:
            x = int(entry_x.get())
            e = float(entry_accuracy.get())# получаем введенный текст, entry- поле
            count = 0
            for n in range(0, 25):
                t = (((-1) ** n) * (x ** (2 * n))) / factorial(2 * n + 1)
                if fabs(t) < e:
                    break
                else:
                    count += t
            label_one["text"] = "Сумма ряда равна: " + str(count)
        except:
            label_one["text"] = "Некорректный ввод"

    lab_6 = Toplevel()
    lab_6.title("Лабораторная работа 6")
    lab_6.geometry("500x500")
    lab_6.configure(bg="beige")
    lab_6.resizable(width=False, height=False)  # нельзя менять размер ячеек

    #создание фрейма
    fr_lab6 = Frame(lab_6, background="beige")
    quest = Label(lab_6, text="Лабораторная работа 6 \n Разработать приложение для вычисления \n суммы ряда Тейлора с заданной точностью ε", bg="beige")
    quest.pack()

    #вывод изображения
    img = Image.open("assets/lab6.png")
    pil_image = img.resize((300, 50))
    fr_lab6.image = ImageTk.PhotoImage(pil_image)
    image_sprite = Label(fr_lab6, image=fr_lab6.image, bg="beige")
    image_sprite.pack()

    #кнопка,текстовое полe и вывод результата
    label_x = Label(fr_lab6, text="Введите X", bg="beige")
    label_x.pack()

    entry_x = Entry(fr_lab6, bg="beige")
    entry_x.pack(padx=6, pady=6)

    label_accuracy = Label(fr_lab6, text="Введите ε", bg="beige")
    label_accuracy.pack()

    entry_accuracy = Entry(fr_lab6, bg="beige")
    entry_accuracy.pack(padx=6, pady=6)

    btn = Button(fr_lab6, text="Запустить", command=show_answer, bg="beige")
    btn.pack(padx=6, pady=6)

    label_one = Label(fr_lab6, bg="beige")
    label_one.pack(padx=6, pady=6)

    label_two =Label(fr_lab6, bg="beige")
    label_two.pack(padx=7, pady=7)

    fr_lab6.pack()

def createWindowLab_7():
    def remove_text():
        label_one.config(text="")
    def show_answer():
        remove_text()
        try:
            a = int(entry_a.get())
            b = int(entry_b.get())
            N = int(entry_n.get())
            e = float(entry_accuracy.get())
            k = (b - a) / N

            data = []
            m = 0

            for x in np.arange(b, a - 0.5, -k):
                count = 0
                t = 0
                for n in range(0, 25):
                    t = (((-1) ** n) * (x ** (2 * n))) / factorial(2 * n + 1)
                    count += t
                    if fabs(t) < e:
                        break
                m += 1

                ab = (m, x, count)
                data.append(ab)

            # определяем столбцы
            columns = ("n", "x", "y")

            tree = Treeview(fr_lab7, columns=columns, show="headings")
            tree.pack(side='left')

            # определяем заголовки
            tree.heading("n", text="N")
            tree.heading("x", text="X")
            tree.heading("y", text="Y")

            tree.column("#1", width=70)
            tree.column("#2", width=70)
            tree.column("#3", width=70)

            # добавляем данные
            for i in data:
                tree.insert(parent='', index='end', values=i)

        except:
            label_one["text"] = "Некорректный ввод"

    lab_7 = Toplevel()
    lab_7.title("Лабораторная работа 7")
    lab_7.geometry("500x500")
    lab_7.configure(bg="beige")
    lab_7.resizable(width=False, height=False)  # нельзя менять размер ячеек

    #создание фрейма
    fr_lab7 = Frame(lab_7, background="beige")
    quest = Label(lab_7, text="Лабораторная работа 7 \n Разработать приложение для вывода таблицы значений \n "
                              "функции y = f(x) в точках, полученных делением отрезка [a,b] на N равных частей", bg="beige")
    quest.pack()

    #вывод изображения
    img = Image.open("assets/lab6.png")
    pil_image = img.resize((300, 50))
    fr_lab7.image = ImageTk.PhotoImage(pil_image)
    image_sprite = Label(fr_lab7, image=fr_lab7.image, bg="beige")
    image_sprite.pack()


    #кнопка,текстовое полe и вывод результата
    label_a = Label(fr_lab7, text="Введите a", bg="beige")
    label_a.pack()

    entry_a = Entry(fr_lab7, bg="beige")
    entry_a.pack(padx=6, pady=6)

    label_b = Label(fr_lab7, text="Введите b", bg="beige")
    label_b.pack()

    entry_b = Entry(fr_lab7, bg="beige")
    entry_b.pack(padx=6, pady=6)

    label_n = Label(fr_lab7, text="Введите N", bg="beige")
    label_n.pack()

    entry_n = Entry(fr_lab7, bg="beige")
    entry_n.pack(padx=6, pady=6)

    label_accuracy = Label(fr_lab7, text="Введите ε", bg="beige")
    label_accuracy.pack()

    entry_accuracy = Entry(fr_lab7, bg="beige")
    entry_accuracy.pack(padx=6, pady=6)

    btn = Button(fr_lab7, text="Запустить", command=show_answer, bg="beige")
    btn.pack(padx=6, pady=6)

    label_one = Label(fr_lab7, bg="beige")
    label_one.pack(padx=6, pady=6)


    fr_lab7.pack()

lab_1 = Button(root, text="lab_1", command=createWindowLab_1, bg="#d6f3c2", activebackground="beige", width=20)
lab_1.pack(anchor=NW, pady=5, padx=20)

lab_2 = Button(text="lab_2", command=createWindowLab_2, bg="#d6f3c2", activebackground="beige", width=20)
lab_2.pack(anchor=NW, pady=5, padx=20)

lab_3 = Button(text="lab_3", command=createWindowLab_3, bg="#d6f3c2", activebackground="beige", width=20)
lab_3.pack(anchor=NW, pady=5, padx=20)

lab_4 = Button(text="lab_4", command=createWindowLab_4, bg="#d6f3c2", activebackground="beige", width=20)
lab_4.pack(anchor=NW, pady=5, padx=20)

lab_5 = Button(text="lab_5",  command=createWindowLab_5, bg="#d6f3c2", activebackground="beige", width=20)
lab_5.pack(anchor=NW, pady=5, padx=20)

lab_6 = Button(text="lab_6", command=createWindowLab_6, bg="#d6f3c2", activebackground="beige", width=20)
lab_6.pack(anchor=NW, pady=5, padx=20)

lab_7 = Button(text="lab_7", command=createWindowLab_7, bg="#d6f3c2", activebackground="beige", width=20)
lab_7.pack(anchor=NW, pady=5, padx=20)

root.mainloop()