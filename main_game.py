from tkinter import *
from screeninfo import get_monitors
WIDTH, HEIGHT = get_monitors()[0].width, get_monitors()[0].height

def main():
    """Главная функция главного модуля.
    Создаёт объекты графического дизайна библиотеки tkinter: окно, холст, фрейм с кнопками, кнопки.
    """
    def Start():
        root.destroy()
        window = Tk()
        window.title("КликКлак")
        space = Canvas(window, width=WIDTH, height=HEIGHT, bg="white")
        space.pack(side=TOP)

    root = Tk()
    root.title("ОхаЁ")
    root['bg']='white'
    root.geometry(f'{WIDTH}x{HEIGHT}')

    button = Button(compound=CENTER,text="Новая игра",
                            font=("Arial Bold", 30),command=Start,
                            bg="white", fg="black",width=20)
    button.pack()
    button.place(relx=0.36, rely=0.25, relwidth=0.25, relheight=0.33)
    root.mainloop()


if __name__ == "__main__":
    main()

