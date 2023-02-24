import cmath
from tkinter import *
from tkinter import ttk
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
            b = int(entry.get())  # получаем введенный текст, entry- поле
            if b == -2:
                label_one["text"] = "Уравнение не имеет решения, введите другое значение переменной b"
            elif b<2:
                z1 = (cmath.sqrt(2 * b + cmath.sqrt(b * b - 4))) / ((cmath.sqrt(b * b - 4)) + b + 2)
                z2 = 1 / (cmath.sqrt(b + 2))
                print("z1 = ", z1, "z2 = ", z2)
                label_one["text"] = "z1 = ", z1
                label_two["text"] = "z2 = ", z2
            else:
                z1 = (sqrt(2 * b + sqrt(b * b - 4))) / ((sqrt(b * b - 4)) + b + 2)
                z2 = 1 / (sqrt(b + 2))
                print("z1 = ", z1, "z2 = ", z2)
                label_one["text"] = "z1 = ", z1
                label_two["text"] = "z2 = ", z2
        except:
            label_one["text"] = "Некорректный ввод"
    lab_1 = Toplevel()
    lab_1.title("Лабораторная работа 1")
    lab_1.geometry("500x400")
    lab_1.configure(bg="beige")
    lab_1.resizable(width=False, height=False)  # нельзя менять размер ячеек

#создание фрейма
    fr_lab1 = Frame(lab_1)
    quest = Label(lab_1, text="fhhfjjgkgk \n jfjjf ")
    quest.pack()

    #вывод изображения

    pil_image = Image.open("assets/Lab1_z1.jpg")
    fr_lab1.image = ImageTk.PhotoImage(pil_image)
    image_sprite = Label(fr_lab1, image=fr_lab1.image)
    image_sprite.pack()

    pil_image1 = Image.open("assets/Lab1_z2.jpg")
    fr_lab1.image1 = ImageTk.PhotoImage(pil_image1)
    image_sprite1 = Label(fr_lab1, image=fr_lab1.image1)
    image_sprite1.pack()

    #кнопка,текстовое полe и вывод результата
    entry = Entry(fr_lab1, )
    entry.pack(padx=6, pady=6)

    btn = Button(fr_lab1, text="Кликк", command=show_answer)
    btn.pack(padx=6, pady=6)

    label_one = Label(fr_lab1)
    label_one.pack(padx=6, pady=6)

    label_two =Label(fr_lab1)
    label_two.pack(padx=7, pady=7)

    fr_lab1.pack()

lab_1 = Button(root, text="lab_1", command=createWindowLab_1, bg="#d6f3c2", activebackground="beige", width=20)
lab_1.pack(anchor=NW, pady=5, padx=20)
lab_2 = Button(text="lab_2", bg="#d6f3c2", activebackground="beige", width=20)
lab_2.pack(anchor=NW, pady=5, padx=20)
lab_3 = Button(text="lab_3", bg="#d6f3c2", activebackground="beige", width=20)
lab_3.pack(anchor=NW, pady=5, padx=20)
lab_4 = Button(text="lab_4", bg="#d6f3c2", activebackground="beige", width=20)
lab_4.pack(anchor=NW, pady=5, padx=20)
lab_5 = Button(text="lab_5", bg="#d6f3c2", activebackground="beige", width=20)
lab_5.pack(anchor=NW, pady=5, padx=20)
lab_6 = Button(text="lab_6", bg="#d6f3c2", activebackground="beige", width=20)
lab_6.pack(anchor=NW, pady=5, padx=20)
lab_7 = Button(text="lab_7", bg="#d6f3c2", activebackground="beige", width=20)
lab_7.pack(anchor=NW, pady=5, padx=20)
root.mainloop()
