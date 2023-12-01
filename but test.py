from tkinter import *
from tkinter import ttk
from screeninfo import get_monitors

root = Tk()
root['bg'] = 'white'
WIDTH, HEIGHT = get_monitors()[0].width, get_monitors()[0].height
root.geometry(f'{WIDTH}x{HEIGHT}')

MONEY = 0
CLICK_VALUE = 1
INFO = StringVar()
INFO.set(f"Баллы: {MONEY}\nБаллы в секунду: {0}\nБаллы за клик: {CLICK_VALUE}")


def give_money():
    '''Вспомогательная функция для кнопки клик, возможно её нужно вызывать каждый тик, а не только при нажатии по кнопке'''
    global MONEY, CLICK_VALUE, INFO
    MONEY += CLICK_VALUE
    INFO.set(f"Баллы: {MONEY}\nБаллы в секунду: {0}\nБаллы за клик: {CLICK_VALUE}")


def normalise_nums(num):
    if num < 1000:
        return str(num)
    if num > 1000 and num < 1000000:
        num = str(num // 1000) + '.' + str(num % 1000)[0] + 'K'
        return num
    if num > 1000000 and num < 1000000000:
        num = str(num // 1000000) + '.' + str(num % 1000000)[0] + 'M'
        return num
    if num > 1000000000 and num < 1000000000000:
        num = str(num // 1000) + '.' + str(num % 1000)[0] + 'B'
        return num


class mine:
    def __init__(self, lvl=0, efficiency=0, cost=0, window=root, pos=1):
        self.pos = pos - 1
        self.lvl = lvl
        self.window = window
        self.efficiency = efficiency
        self.cost = cost
        self.inf = StringVar()
        if self.pos==0: self.inf.set(f'Купить студента: {0}\nУровень: {self.efficiency}\nПроизводительность: {0}\nСтоимость: {0}') #FIXME нужно вместо ноликов что то внятное написать
        elif self.pos == 1: self.inf.set(f'Купить семинариста: {0}\nУровень: {self.efficiency}\nПроизводительность: {0}\nСтоимость: {0}')
        elif self.pos == 2: self.inf.set(f'Купить кафедру: {0}\nУровень: {self.efficiency}\nПроизводительность: {0}\nСтоимость: {0}')
        self.text = Button(window, textvariable=self.inf, width=10, height=5, state=["disabled"])
        self.text.place(relx=0.1, rely=0.34 + self.pos * 0.15, relwidth=0.18, relheight=0.13)

        self.btn = Button(window, text='lvl up', command=self.lvluped, width=10, height=5)
        self.btn.place(relx=0.28, rely=0.34 + self.pos * 0.15, relwidth=0.08, relheight=0.13)
    def __str__(self):
        return str(self.pos + 1)

    def lvluped(self):
        self.efficiency += 1
        print('lvl up', self, self.efficiency)
        if self.pos==0: self.inf.set(f'Купить студента: {0}\nУровень: {self.efficiency}\nПроизводительность: {0}\nСтоимость: {0}')
        elif self.pos == 1: self.inf.set(f'Купить семинариста: {0}\nУровень: {self.efficiency}\nПроизводительность: {0}\nСтоимость: {0}') #FIXME та же херня что и сверху
        elif self.pos == 2: self.inf.set(f'Купить кафедру: {0}\nУровень: {self.efficiency}\nПроизводительность: {0}\nСтоимость: {0}')
    def mining(self):
        '''Первая шахта должна добывать ресурсы, вторая и третья должны повышать уровень предыдущей'''
        # FIXME хз как у нас должна добыча баллов происхоидить, полагаю зависит от уровня и позиции (может тупо if'ами оформить)
        pass


m1 = mine(pos=1)
m2 = mine(pos=2)
m3 = mine(pos=3)

click_button = Button(compound=CENTER, text="Клик",
                      font=("Comic Sans bold", 16), command=give_money, #тут вызывается кнопка Клик
                      bg="white", fg="black", width=20)
click_button.pack()
click_button.place(relx=0.05, rely=0.05, relwidth=0.2, relheight=0.2)
label = ttk.Label(textvariable=INFO, font=("Comic 16"))   #тут выводится основная информация
label.pack()
label.place(relx=0.5, rely=0.05, relwidth=0.2, relheight=0.2)

root.update()
root.mainloop()
