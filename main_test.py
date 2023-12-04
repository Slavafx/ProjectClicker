from tkinter import *
from tkinter import ttk
from screeninfo import get_monitors
import time
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

from but_test import *
WIDTH, HEIGHT = get_monitors()[0].width, get_monitors()[0].height

def main():
    """Главная функция главного модуля.
    Создаёт объекты графического дизайна библиотеки tkinter: окно, холст, фрейм с кнопками, кнопки.
    """
    def Start():
        window.destroy()
        root = Tk()
        root.title("КликКлак")
        root['bg'] = 'white'
        WIDTH, HEIGHT = get_monitors()[0].width, get_monitors()[0].height
        root.geometry(f'{WIDTH}x{HEIGHT}')

        MONEY = 0
        CLICK_VALUE = 1

        old_time = 0
        gm = Game_Session(cost1=5, cost2=100, cost3=1000, cost4=100000, cost5=10000000, cost6=100000000,
                          cost7=10000000000, cost8=100000000000, cost9=10000000000000)

        flag = 0
        start_time = time.time()
        while True:

            new_time = time.time()
            if new_time - old_time >= 1:
                gm.update_money(1)
                old_time = new_time

                gm.MoneyData = np.append(gm.MoneyData, gm.money)
                gm.TimeData = np.append(gm.TimeData, new_time - start_time)
                gm.IncomeData = np.append(gm.IncomeData, gm.m1.efficiency)

                fig, ax = plt.subplots()
                ax.plot(gm.TimeData, gm.MoneyData, 'k')
                fig.savefig('a.png')

                image = Image.open("a.png")
                width, height = image.size
                image = image.resize((int(WIDTH * 0.27 // 1), int(WIDTH * 0.2025 // 1)))

                photo = ImageTk.PhotoImage(image)
                img = Button(root, image=photo, state=["disabled"])
                img.place(relx=0.7, rely=0.05)
                image.close()

                fig2, ax2 = plt.subplots()
                ax2.plot(gm.TimeData, gm.IncomeData, 'k')
                fig2.savefig('b.png')

                image2 = Image.open("b.png")
                width2, height2 = image2.size
                image2 = image2.resize((int(WIDTH * 0.27 // 1), int(WIDTH * 0.2025 // 1)))

                photo2 = ImageTk.PhotoImage(image2)
                img2 = Button(root, image=photo2, state=["disabled"])
                img2.place(relx=0.7, rely=0.45)
                image2.close()

            root.update()

    window = Tk()
    print(1)
    window.title("ОхаЁ")
    window['bg']='white'
    window.geometry(f'{WIDTH}x{HEIGHT}')

    button = Button(compound=CENTER,text="Новая игра",
                            font=("Arial Bold", 30),command=Start,
                            bg="white", fg="black",width=20)
    button.pack()
    button.place(relx=0.36, rely=0.25, relwidth=0.25, relheight=0.33)
    window.mainloop()



if __name__ == "__main__":
    main()
