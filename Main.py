# Case-study #6
# Developers:   Aksenov A. (55%),
#               Soloveychik D. (60%),
#               Labuzov A. (48%)
import turtle as t
from math import sqrt


def get_num_hexagons():
    """
    функция для ввода количества шестиугольников, предусматривающая проверку ввода данных.
    """
    a = 0
    n = input("Пожалуйста, введите количество шестиугольников, располагаемых в ряд: ")
    while a == 0:
        try:
            n = int(n)
            if n > 3 and n < 21:
                return n
                break
            else:
                n = input("Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: ")
        except ValueError:
            n = input("Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: ")


def get_color_choice(n):
    """
    Функция для выбора цвета заливки шестиугольника
    """
    if n==1:
        color=input("Введите первый цвет: ").lower()
    else:
        color=input("Введите второй цвет: ").lower()
    a=0
    while a==0:
        if color == "красный":
            return "red"
            break
        elif color == "синий":
            return "blue"
            break
        elif color == "зеленый":
            return "green"
            break
        elif color == "желтый":
            return "yellow"
            break
        elif color == "оранжевый":
            return "orange"
            break
        elif color == "фиолетовый":
            return "purple"
            break
        elif color == "розовый":
            return "pink"
            break
        else:
            color = input(color+" не является верным значением. Пожалуйста, повторите попытку: ").lower()



            


def turtle_area(n):
    height = 500 * (3 * n + 1) / (sqrt(3) * (2 * n + 1))
    t.up()
    t.goto(-100, -100)
    t.down()
    t.pensize(3)
    t.left(90)
    t.fd(height)
    t.right(90)
    t.fd(500)
    t.right(90)
    t.fd(height)
    t.right(90)
    t.fd(500)
    return height


def right_fd(angle, side_len, times):
    while times != 0:
        t.right(angle)
        t.fd(side_len)
        times -= 1


def draw_hexagon(y_side, color):
    t.down()
    t.setheading(-90)
    t.up()
    t.fd(y_side)
    t.down()
    t.pencolor("black")
    t.fillcolor(color)
    t.begin_fill()
    t.left(120)
    t.fd(2 * y_side)
    right_fd(60, 2 * y_side, 6)
    t.end_fill()


def draw_hexagons(x, y, count, color1, color2):
    """
    В данной функции 72.17 получена путем решения уравнения, где 500 = 8x, x = 62.5, что равно половине длины шестиугольника, а сторона шестиугольника = 62,5/cos(30) = 72,17
    далее функция адаптируется к количеству путем домножения стороны на коэф=4/кол-во шестиугольников
    """
    x_side = 500 / (2 * count + 1)
    y_side = x_side / sqrt(3)
    for j in range(0, count):
        t.up()
        t.goto(x, y)
        draw_hexagon(y_side, color1)
        x += 2 * x_side
    x = -100
    y -= 4 * y_side
    t.up()
    t.goto(x, y)
    t.down()

    for i in range(2, count + 1):
        if i % 2 == 1:
            for j in range(0, count):
                t.up()
                t.goto(x, y + 2 * y_side)
                draw_hexagon(y_side, color1)
                x += 2 * x_side
            y += 2 * y_side
        else:
            for j in range(0, count):
                t.up()
                t.goto(x + x_side, y + y_side)
                draw_hexagon(y_side, color2)
                x += 2 * x_side
        x = -100
        y -= 4 * y_side
        t.up()
        t.goto(x, y)
        t.down()


count = get_num_hexagons()
height = turtle_area(count)
print("Доступный набор цветов:")
print(*(color for color in ('красный', 'синий', 'зеленый', 'желтый', 'оранжевый', 'фиолетовый', 'розовый')), sep='\n')
color1 = get_color_choice(1)
color2 = get_color_choice(2)
draw_hexagons(-100, height-100, count, color1, color2)

t.mainloop()

