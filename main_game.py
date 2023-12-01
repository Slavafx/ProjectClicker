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
        window.title("Новое окно")
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
    button.place(x=WIDTH//2.8, y=HEIGHT//4, width=WIDTH//4, height=HEIGHT//3)
    root.mainloop()


if __name__ == "__main__":
    main()

