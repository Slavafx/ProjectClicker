from tkinter import *
from screeninfo import get_monitors
root = Tk()
root['bg'] = 'white'
WIDTH, HEIGHT = get_monitors()[0].width, get_monitors()[0].height
root.geometry(f'{WIDTH}x{HEIGHT}')

def normalise_nums(num):
    if num < 1000:
        return str(num)
    if num > 1000 and num < 1000000:
        num = str(num//1000) + '.' + str(num%1000)[0] + 'K'
        return num
    if num > 1000000 and num < 1000000000:
        num = str(num//1000000) + '.' + str(num%1000000)[0] + 'M'
        return num
    if num > 1000000000 and num < 1000000000000:
        num = str(num//1000) + '.' + str(num%1000)[0] + 'B'
        return num




class mine:
    def __init__(self, lvl=0, efficiency=0, cost=0, window=root, WIDTH=WIDTH, HEIGHT=HEIGHT, pos=1):
        self.pos = pos-1
        self.lvl = lvl
        self.window = window
        self.efficiency = efficiency
        self.cost = cost
        self.text = Button(window, text=f'ШАХТА {self.efficiency}', width=10, height=5, state=["disabled"])
        self.text.place(relx=0.1, rely = 0.34 + self.pos*0.15, relwidth=0.18, relheight=0.13)



        self.btn = Button(window, text='lvl up', command=self.lvluped, width=10, height=5)
        self.btn.place(relx = 0.28, rely = 0.34 + self.pos*0.15, relwidth = 0.08, relheight = 0.13)




    def lvluped(self):
        self.efficiency += 1
        print('lvl up', self)

m1 = mine(pos=1)
m2 = mine(pos=2)
m3 = mine(pos=3)

root.update()
root.mainloop()







