import tkinter
def main():
    """Главная функция главного модуля.
    Создаёт объекты графического дизайна библиотеки tkinter: окно, холст, фрейм с кнопками, кнопки.
    """

    print('Modelling started!')
    physical_time = 0

    root = tkinter.Tk()
    # космическое пространство отображается на холсте типа Canvas
    space = tkinter.Canvas(root, width=600, height=400, bg="red")
    space.pack(side=tkinter.TOP)





    root.mainloop()
    print('Modelling finished!')

if __name__ == "__main__":
    main()

