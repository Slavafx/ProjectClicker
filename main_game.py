import tkinter
from screeninfo import get_monitors
WIDTH, HEIGHT = get_monitors()[0].width, get_monitors()[0].height


def main():
    """Главная функция главного модуля.
    Создаёт объекты графического дизайна библиотеки tkinter: окно, холст, фрейм с кнопками, кнопки.
    """


    def Start():
        root.destroy()
        window = tkinter.Tk()
        window.title("Новое окно")
        space = tkinter.Canvas(window, width=WIDTH, height=HEIGHT, bg="blue")
        space.pack(side=tkinter.TOP)

    root = tkinter.Tk()
    root.title("ОхаЁ")
    root['bg']='blue'
    root.geometry(f'{WIDTH}x{HEIGHT}')

    button = tkinter.Button(compound=tkinter.CENTER,text="Новая игра",
                            font=("Arial Bold", 30),command=Start,
                            bg="blue", fg="yellow",width=20)
    button.pack()











    root.mainloop()

if __name__ == "__main__":
    main()

