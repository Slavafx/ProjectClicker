from tkinter import *
from tkinter import ttk
from screeninfo import get_monitors
import time
import numpy as np
import matplotlib.pyplot as plt
from math import *
from PIL import Image, ImageTk

root = Tk()
root['bg'] = 'white'
WIDTH, HEIGHT = get_monitors()[0].width, get_monitors()[0].height
root.geometry(f'{WIDTH}x{HEIGHT}')

MONEY = 0
CLICK_VALUE = 1






def normalise_nums(num):
    if num < 1000:
        num = str(round(num, 1))
        return num
    if num > 1000 and num < 1000000:
        num = str(round((num / 1000), 1)) + 'K'
        return num
    if num > 1000000 and num < 1000000000:
        num = str(round((num / 1000000), 1)) + 'M'
        return num
    if num > 1000000000 and num < 1000000000000:
        num = str(round((num / 1000000000), 1)) + 'B'
        return num
    if num > 1000000000000 and num < 1000000000000000:
        num = str(round((num / 1000000000000), 1)) + 'T'
        return num
    if num > 1000000000000000 and num < 11000000000000000000:
        num = str(round((num / 1000000000000000), 1)) + 'Kv'
        return num
    if num > 1000000000000000000 and num < 1000000000000000000000:
        num = str(round((num / 1000000000000000000), 1)) + 'Sep'
        return num
    if num > 1000000000000000000000:
        num = str(round((num / 1000000000000000000000), 1)) + 'Six'
        return num


class mine:
    def __init__(self, lvl=0, efficiency=0, cost=0, window=root, pos=1, session = 0):
        if pos < 4:
            self.game_session = session
            self.pos = pos - 1
            self.lvl = lvl
            self.window = window
            self.efficiency = efficiency
            self.cost = cost
            self.inf = StringVar()
            if self.pos==0: self.inf.set(f'Производство 1: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')
            elif self.pos == 1: self.inf.set(f'Производство 2: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')
            elif self.pos == 2: self.inf.set(f'Производство 3: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')
            self.text = Button(window, textvariable=self.inf, width=10, height=5, state=["disabled"])
            self.text.place(relx=0.03, rely=0.34 + self.pos * 0.15, relwidth=0.12, relheight=0.13)

            self.btn = Button(window, text='lvl up', command=self.lvluped, width=10, height=5)
            self.btn.place(relx=0.15, rely=0.34 + self.pos * 0.15, relwidth=0.08, relheight=0.13)
            self.pos += 1


        elif pos < 7:
            self.game_session = session
            self.pos = pos - 4
            self.lvl = lvl
            self.window = window
            self.efficiency = efficiency
            self.cost = cost
            self.inf = StringVar()
            if self.pos == 0:
                self.inf.set(
                    f'Производство 4\nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')
            elif self.pos == 1:
                self.inf.set(
                    f'Производство 5: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')
            elif self.pos == 2:
                self.inf.set(
                    f'Производство 6 \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')
            self.text = Button(window, textvariable=self.inf, width=10, height=5, state=["disabled"])
            self.text.place(relx=0.25, rely=0.34 + self.pos * 0.15, relwidth=0.12, relheight=0.13)

            self.btn = Button(window, text='lvl up', command=self.lvluped, width=10, height=5)
            self.btn.place(relx=0.37, rely=0.34 + self.pos * 0.15, relwidth=0.08, relheight=0.13)
            self.pos += 4


        else:
            self.game_session = session
            self.pos = pos - 7
            self.lvl = lvl
            self.window = window
            self.efficiency = efficiency
            self.cost = cost
            self.inf = StringVar()
            if self.pos == 0:
                self.inf.set(
                    f'Производство 7: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')
            elif self.pos == 1:
                self.inf.set(
                    f'производство 8: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')
            elif self.pos == 2:
                self.inf.set(
                    f'Производство 9: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')
            self.text = Button(window, textvariable=self.inf, width=10, height=5, state=["disabled"])
            self.text.place(relx=0.47, rely=0.34 + self.pos * 0.15, relwidth=0.12, relheight=0.13)

            self.btn = Button(window, text='lvl up', command=self.lvluped, width=10, height=5)
            self.btn.place(relx=0.59, rely=0.34 + self.pos * 0.15, relwidth=0.08, relheight=0.13)
            self.pos += 7



    def __str__(self):
        return str(self.pos + 1)

    def lvluped(self, lvlup_by_another_mine = 0, num_of_levels = 1):

        if not lvlup_by_another_mine:
            if self.game_session.money >= self.cost:
                self.game_session.money -= self.cost
                self.cost *= 1.9
                self.lvl += 1
                if self.efficiency == 0:
                    self.efficiency += 1
                else:
                    self.efficiency += 1


                if self.pos == 1:
                    self.inf.set(
                        f'Производство 1: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')

                elif self.pos == 2:
                    self.inf.set(
                        f'Производство 2: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')

                elif self.pos == 3:
                    self.inf.set(
                        f'Производство 3: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')

                elif self.pos == 4:
                    self.inf.set(
                        f'Производство 4: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')

                elif self.pos == 5:
                    self.inf.set(
                        f'Производство 5: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')

                elif self.pos == 6:
                    self.inf.set(
                        f'Производство 6: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')

                elif self.pos == 7:
                    self.inf.set(
                        f'Производство 7: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')

                elif self.pos == 8:
                    self.inf.set(
                        f'Производство 8: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')

                elif self.pos == 9:
                    self.inf.set(
                        f'Производство 9: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')



                self.game_session.INFO.set(
                    f"Баллы: {normalise_nums(self.game_session.money)}\nБаллы в секунду: {normalise_nums(self.game_session.mon_per_second)}\nБаллы за клик: {normalise_nums(self.game_session.mon_per_click)}")
            else:
                pass

        else:
            if True:
                self.game_session.money -= 0

                self.lvl += 1*num_of_levels
                if self.efficiency == 0:
                    self.efficiency += 1*num_of_levels
                else:
                    self.efficiency += 1*num_of_levels

                if self.pos == 1:
                    self.inf.set(
                        f'Производство 1: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')

                elif self.pos == 2:
                    self.inf.set(
                        f'Производство 2: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')

                elif self.pos == 3:
                    self.inf.set(
                        f'Производство 3: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')

                elif self.pos == 4:
                    self.inf.set(
                        f'Производство 4: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')

                elif self.pos == 5:
                    self.inf.set(
                        f'Производство 5: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')

                elif self.pos == 6:
                    self.inf.set(
                        f'Производство 6: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')

                elif self.pos == 7:
                    self.inf.set(
                        f'Производство 7: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')

                elif self.pos == 8:
                    self.inf.set(
                        f'Производство 8: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')

                elif self.pos == 9:
                    self.inf.set(
                        f'Производство 9: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')

                self.game_session.INFO.set(
                    f"Баллы: {normalise_nums(self.game_session.money)}\nБаллы в секунду: {normalise_nums(self.game_session.mon_per_second)}\nБаллы за клик: {normalise_nums(self.game_session.mon_per_click)}")

    def mining(self, k):
        '''Первая шахта должна добывать ресурсы, вторая и третья должны повышать уровень предыдущей'''
        if self.pos == 1:
            self.game_session.money += self.efficiency*k

        if self.pos == 2:

            self.game_session.m1.lvluped(lvlup_by_another_mine = 1, num_of_levels=self.efficiency*k)

        if self.pos == 3:

            self.game_session.m2.lvluped(lvlup_by_another_mine= 1, num_of_levels=self.efficiency*k)

        if self.pos == 4:

            self.game_session.m3.lvluped(lvlup_by_another_mine= 1, num_of_levels=self.efficiency*k)

        if self.pos == 5:

            self.game_session.m4.lvluped(lvlup_by_another_mine= 1, num_of_levels=self.efficiency*k)

        if self.pos == 6:

            self.game_session.m5.lvluped(lvlup_by_another_mine= 1, num_of_levels=self.efficiency*k)

        if self.pos == 7:

            self.game_session.m6.lvluped(lvlup_by_another_mine= 1, num_of_levels=self.efficiency*k)

        if self.pos == 8:

            self.game_session.m7.lvluped(lvlup_by_another_mine= 1, num_of_levels=self.efficiency*k)

        if self.pos == 9:

            self.game_session.m8.lvluped(lvlup_by_another_mine= 1, num_of_levels=self.efficiency*k)






class Game_Session:
    def __init__(self, cost1, cost2, cost3, cost4, cost5, cost6, cost7, cost8, cost9):
        print(cost9, cost8)
        self.m1 = mine(pos=1, cost = cost1, session=self)
        self.m2 = mine(pos=2, cost = cost2, session=self)
        self.m3 = mine(pos=3, cost = cost3, session=self)

        self.m4 = mine(pos=4, cost=cost4, session=self)
        self.m5 = mine(pos=5, cost=cost5, session=self)
        self.m6 = mine(pos=6, cost=cost6, session=self)

        self.m7 = mine(pos=7, cost=cost7, session=self)
        self.m8 = mine(pos=8, cost=cost8, session=self)
        self.m9 = mine(pos=9, cost=cost9, session=self)


        self.TimeData = np.array([0])
        self.MoneyData = np.array([0])
        self.IncomeData = np.array([0])







        self.money = 0

        self.mon_per_click = 1

        self.mon_per_second = 0

        self.INFO = StringVar()
        self.INFO.set(f"Баллы: {self.money}\nБаллы в секунду: {self.mon_per_second}\nБаллы за клик: {self.mon_per_click}")

        self.click_button = Button(compound=CENTER, text="Клик",
                                   font=("Comic Sans bold", 16), command=self.give_money,  # тут вызывается кнопка Клик
                                   fg="black", width=20)
        self.click_button.pack()
        self.click_button.place(relx=0.03, rely=0.08, relwidth=0.2, relheight=0.2)
        label = ttk.Label(textvariable=self.INFO, font=("Comic 16"))  # тут выводится основная информация
        label.pack()
        label.place(relx=0.47, rely=0.08, relwidth=0.2, relheight=0.2)

    def give_money(self):

        '''Вспомогательная функция для кнопки клик, возможно её нужно вызывать каждый тик, а не только при нажатии по кнопке'''
        self.money += self.mon_per_click

        self.INFO.set(f"Баллы: {normalise_nums(self.money)}\nБаллы в секунду: {normalise_nums(self.mon_per_second)}\nБаллы за клик: {normalise_nums(self.mon_per_click)}")




    def update_money(self, k):
        self.m1.mining(k)
        self.m2.mining(k)
        self.m3.mining(k)
        self.m4.mining(k)
        self.m5.mining(k)
        self.m6.mining(k)
        self.m7.mining(k)
        self.m8.mining(k)
        self.m9.mining(k)
        self.mon_per_second = self.m1.efficiency
        self.INFO.set(
            f"Баллы: {normalise_nums(self.money)}\nБаллы в секунду: {normalise_nums(self.mon_per_second)}\nБаллы за клик: {normalise_nums(self.mon_per_click)}")


old_time = 0
gm = Game_Session(cost1=5, cost2=100, cost3=1000, cost4=100000, cost5=10000000, cost6=100000000, cost7=10000000000, cost8=100000000000, cost9=10000000000000)



flag = 0
start_time = time.time()
while True:

    new_time = time.time()
    if new_time - old_time >= 1:
        gm.update_money(1)
        old_time = new_time

        gm.MoneyData = np.append(gm.MoneyData, gm.money)
        gm.TimeData = np.append(gm.TimeData, new_time - start_time)
        gm.IncomeData = np.append(gm.IncomeData, log(1+gm.m1.efficiency))

        fig, ax = plt.subplots()
        ax.plot(gm.TimeData, gm.MoneyData, 'k')
        fig.savefig('a.png')

        image = Image.open("a.png")
        width, height = image.size
        image = image.resize((int(WIDTH*0.27//1), int(WIDTH*0.2025//1)))


        photo = ImageTk.PhotoImage(image)
        img = Button(root, image=photo, state=["disabled"])
        img.place(relx = 0.7, rely = 0.05)
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

        plt.close(fig = 'all')




    root.update()


