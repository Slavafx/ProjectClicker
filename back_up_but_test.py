from tkinter import *
from tkinter import ttk
from screeninfo import get_monitors
import time

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
    if num > 1000000000:
        num = str(round((num / 1000000000), 1)) + 'B'
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
            if self.pos==0: self.inf.set(f'Купить студента: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')
            elif self.pos == 1: self.inf.set(f'Купить семинариста: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')
            elif self.pos == 2: self.inf.set(f'Купить кафедру: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')
            self.text = Button(window, textvariable=self.inf, width=10, height=5, state=["disabled"])
            self.text.place(relx=0.05, rely=0.34 + self.pos * 0.15, relwidth=0.13, relheight=0.13)

            self.btn = Button(window, text='lvl up', command=self.lvluped, width=10, height=5)
            self.btn.place(relx=0.18, rely=0.34 + self.pos * 0.15, relwidth=0.08, relheight=0.13)
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
                    f'Купить студента: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')
            elif self.pos == 1:
                self.inf.set(
                    f'Купить семинариста: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')
            elif self.pos == 2:
                self.inf.set(
                    f'Купить кафедру: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')
            self.text = Button(window, textvariable=self.inf, width=10, height=5, state=["disabled"])
            self.text.place(relx=0.1, rely=0.34 + self.pos * 0.15, relwidth=0.18, relheight=0.13)

            self.btn = Button(window, text='lvl up', command=self.lvluped, width=10, height=5)
            self.btn.place(relx=0.18, rely=0.34 + self.pos * 0.15, relwidth=0.08, relheight=0.13)
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
                    f'Купить студента: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')
            elif self.pos == 1:
                self.inf.set(
                    f'Купить семинариста: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')
            elif self.pos == 2:
                self.inf.set(
                    f'Купить кафедру: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')
            self.text = Button(window, textvariable=self.inf, width=10, height=5, state=["disabled"])
            self.text.place(relx=0.1, rely=0.34 + self.pos * 0.15, relwidth=0.18, relheight=0.13)

            self.btn = Button(window, text='lvl up', command=self.lvluped, width=10, height=5)
            self.btn.place(relx=0.31, rely=0.34 + self.pos * 0.15, relwidth=0.08, relheight=0.13)



    def __str__(self):
        return str(self.pos + 1)

    def lvluped(self, lvlup_by_another_mine = 0, num_of_levels = 1):

        if not lvlup_by_another_mine:
            if self.game_session.money >= self.cost:
                self.game_session.money -= self.cost
                self.cost *= 1.3
                self.lvl += 1
                if self.efficiency == 0:
                    self.efficiency += 1
                else:
                    self.efficiency += 1


                if self.pos == 0:
                    self.inf.set(
                        f'Купить студента: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')
                elif self.pos == 1:
                    self.inf.set(
                        f'Купить семинариста: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')
                elif self.pos == 2:
                    self.inf.set(
                        f'Купить кафедру: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')

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

                if self.pos == 0:
                    self.inf.set(
                        f'Купить студента: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')
                elif self.pos == 1:
                    self.inf.set(
                        f'Купить семинариста: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')
                elif self.pos == 2:
                    self.inf.set(
                        f'Купить кафедру: \nУровень: {normalise_nums(self.lvl)}\nПроизводительность: {normalise_nums(self.efficiency)}\nСтоимость: {normalise_nums(self.cost)}')

                self.game_session.INFO.set(
                    f"Баллы: {normalise_nums(self.game_session.money)}\nБаллы в секунду: {normalise_nums(self.game_session.mon_per_second)}\nБаллы за клик: {normalise_nums(self.game_session.mon_per_click)}")

    def mining(self, k):
        '''Первая шахта должна добывать ресурсы, вторая и третья должны повышать уровень предыдущей'''
        if self.pos == 0:
            self.game_session.money += self.efficiency*k

        if self.pos == 1:

            self.game_session.m1.lvluped(lvlup_by_another_mine = 1, num_of_levels=self.efficiency*k)

        if self.pos == 2:

            self.game_session.m2.lvluped(lvlup_by_another_mine= 1, num_of_levels=self.efficiency*k)






class Game_Session:
    def __init__(self, cost1, cost2, cost3):

        self.m1 = mine(pos=1, cost = cost1, session=self)
        self.m2 = mine(pos=2, cost = cost2, session=self)
        self.m3 = mine(pos=3, cost = cost3, session=self)





        self.money = 0

        self.mon_per_click = 1

        self.mon_per_second = 0

        self.INFO = StringVar()
        self.INFO.set(f"Баллы: {self.money}\nБаллы в секунду: {self.mon_per_second}\nБаллы за клик: {self.mon_per_click}")

        self.click_button = Button(compound=CENTER, text="Клик",
                                   font=("Comic Sans bold", 16), command=self.give_money,  # тут вызывается кнопка Клик
                                   fg="black", width=20)
        self.click_button.pack()
        self.click_button.place(relx=0.05, rely=0.05, relwidth=0.21, relheight=0.2)
        label = ttk.Label(textvariable=self.INFO, font=("Comic 16"))  # тут выводится основная информация
        label.pack()
        label.place(relx=0.5, rely=0.05, relwidth=0.2, relheight=0.2)

    def give_money(self):

        '''Вспомогательная функция для кнопки клик, возможно её нужно вызывать каждый тик, а не только при нажатии по кнопке'''
        self.money += self.mon_per_click

        self.INFO.set(f"Баллы: {normalise_nums(self.money)}\nБаллы в секунду: {normalise_nums(self.mon_per_second)}\nБаллы за клик: {normalise_nums(self.mon_per_click)}")




    def update_money(self, k):
        self.m1.mining(k)
        self.m2.mining(k)
        self.m3.mining(k)
        self.mon_per_second = self.m1.efficiency
        self.INFO.set(
            f"Баллы: {normalise_nums(self.money)}\nБаллы в секунду: {normalise_nums(self.mon_per_second)}\nБаллы за клик: {normalise_nums(self.mon_per_click)}")


old_time = 0
gm = Game_Session(cost1=2, cost2=10, cost3=100)




while True:
    new_time = time.time()
    if new_time - old_time >= 0.5:
        gm.update_money(0.5)
        old_time = new_time



    root.update()


