from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image, ImageTk

root = Tk()

# создаем рабочую область
frame = Frame(root)
frame.grid()

TimeData = np.array([0])
MoneyData = np.array([0])

for i in range(1000):
    print(i)
    TimeData = np.append(TimeData, [i])
    MoneyData = np.append(MoneyData, [i*np.sin(i)])
    fig, ax = plt.subplots()
    ax.plot(TimeData, MoneyData, 'k')
    fig.savefig('a.png')


    canvas = Canvas(root, height=180, width=240)
    image = Image.open("a.png")
    width, height = image.size
    image = image.resize((240,180))

    photo = ImageTk.PhotoImage(image)
    image2 = canvas.create_image(0, 0, anchor='nw',image=photo)
    canvas.grid(row=2,column=1)
    image.close()


    print(MoneyData)
    root.update()