import tkinter
from screeninfo import get_monitors
WIDTH, HEIGHT = get_monitors()[0].width, get_monitors()[0].height
def main():
    """Главная функция главного модуля.
    Создаёт объекты графического дизайна библиотеки tkinter: окно, холст, фрейм с кнопками, кнопки.
    """

    print('Modelling started!')
    physical_time = 0

    root = tkinter.Tk()
    space = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg="red")
    space.pack(side=tkinter.TOP)





    root.mainloop()
    print('Modelling finished!')

if __name__ == "__main__":
    main()

