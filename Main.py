# Case-study #6
# Developers:   Aksenov A. (%),
#               Soloveychik D. (%),
#               Labuzov A. (%)
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

def get_color_choice(color):
    """
    Функция для выбора цвета заливки шестиугольника
    """
    while True:
        if color == "красный" or "синий" or "зеленый" or "желтый" or "оранжевый" or "фиолетовый" or "розовый":
            if color == "красный":
                return "red"
            if color == "синий":
                return "blue"
            if color == "зеленый":
                return "green"
            if color == "желтый":
                return "yellow"
            if color == "оранжевый":
                return "orange"
            if color == "фиолетовый":
                return "purple"
            if color == "розовый":
                return "pink"
        else:
            color = input(color, "не является верным значением. Пожалуйста, повторите попытку:")

def turtle_area():
    t.up()
    t.goto(-100, -100)
    t.down()
    t.pensize(3)
    t.left(90)
    t.fd(500)
    t.right(90)
    t.fd(500)
    t.right(90)
    t.fd(500)
    t.right(90)
    t.fd(500)


def right_fd(angle, side_len, times):
    while times != 0:
        t.right(angle)
        t.fd(side_len)
        times -= 1


def draw_hexagon(x, y, count, color1, color2):
    """
    В данной функции 72.17 получена путем решения уравнения, где 500=8x,x=62.5, что равно половине длинны шестиугольника, а сторона шестиугольника=62,5/cos(30)=72,17
    далее функция адаптируется к количеству путем домножения стороны на коэф=4/кол-во шестиугольников
    """
    for j in range(0, count):
        t.up()
        t.goto(x, y)
        t.down()
        x_side = (72.17 * 4 / count * sqrt(3)) / 2
        y_side = 72.17 * 4 / count / 2
        t.setheading(-90)
        t.up()
        t.fd(y_side)
        t.down()
        t.pencolor("black")
        t.fillcolor(color1)
        t.begin_fill()
        t.left(120)
        t.fd(72.17 * 4 / count)
        right_fd(60, 72.17 * 4 / count, 6)
        t.end_fill()
        x = x + (125 * (4 / count))
    x = -100
    y = y - (125 * (4 / count))
    t.up()
    t.goto(x, y)
    t.down()

    for i in range(2, count + 1):
        if i % 2 == 1:
            for j in range(0, count):
                t.up()
                t.goto(x, y + 10 * 4 / count)
                t.down()
                x_side = (72.17 * 4 / count * sqrt(3)) / 2
                y_side = 72.17 * 4 / count / 2
                t.setheading(-90)
                t.up()
                t.fd(y_side)
                t.down()
                t.pencolor("black")
                t.fillcolor(color1)
                t.begin_fill()
                t.left(120)
                t.fd(72.17 * 4 / count)
                right_fd(60, 72.17 * 4 / count, 6)
                t.end_fill()
                x = x + (125 * (4 / count))
        else:
            for j in range(0, count):
                t.up()
                t.goto(x + 62 * 4 / count, y + 10 * 4 / count)
                t.down()
                x_side = (72.17 * 4 / count * sqrt(3)) / 2
                y_side = 72.17 * 4 / count / 2
                t.setheading(-90)
                t.up()
                t.fd(y_side)
                t.down()
                t.pencolor("black")
                t.fillcolor(color2)
                t.begin_fill()
                t.left(120)
                t.fd(72.17 * 4 / count)
                right_fd(60, 72.17 * 4 / count, 6)
                t.end_fill()
                x = x + (125 * (4 / count))
        x = -100
        y = y - (115 * (4 / count))
        t.up()
        t.goto(x, y)
        t.down()


turtle_area()
count = get_num_hexagons()
print("Доступный набор цветов:")
print(*(color for color in ('красный', 'синий', 'зеленый', 'желтый', 'оранжевый', 'фиолетовый', 'розовый')), sep='\n')
color1 = get_color_choice(input("Пожалуйста, введите первый цвет:").lower())
color2 = get_color_choice(input("Пожалуйста, введите второй цвет:").lower())
draw_hexagon(-100, 397, count, color1, color2)

t.mainloop()
