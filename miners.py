from tkinter import *
root = Tk()
class mine:
    def __init__(self, lvl=0, efficiency=0, cost=0, window=root, pos=1):
        self.pos = pos - 1
        self.lvl = lvl
        self.window = window
        self.efficiency = efficiency
        self.cost = cost
        self.text = Button(window, text=f'ШАХТА {self.efficiency}', width=10, height=5, state=["disabled"])
        self.text.place(relx=0.1, rely=0.34 + self.pos * 0.15, relwidth=0.18, relheight=0.13)

        self.btn = Button(window, text='lvl up', command=self.lvluped, width=10, height=5)
        self.btn.place(relx=0.28, rely=0.34 + self.pos * 0.15, relwidth=0.08, relheight=0.13)

    def __str__(self):
        return str(self.pos + 1)

    def lvluped(self):
        self.efficiency += 1
        print('lvl up', self)

    def mining(self):
        '''Первая шахта должна добывать ресурсы, вторая и третья должны повышать уровень предыдущей
        зависит от параметра loc, efficientcy
        '''
        pass