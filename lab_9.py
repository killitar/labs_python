#N1 
import math
import turtle as tr


def Func(x):
    y = 0
    
    if x<-9:
        y = None
    elif (x >= -9) and (x < -5):
        y = -math.sqrt(4 - (x + 7) ** 2) + 2
    elif x >= -5 and x < -4:
        y = 2
    elif x >= -4 and x < 0:
        y = -x / 2
    elif x >= 0 and x < math.pi:
        y = math.sin(x)
    elif x >= math.pi and x <= 5:
        y = x
    elif x>5:
        y = None
    return y


def Axis(txy, ax="X"):
    a = txy[0]
    b = txy[1]

    tr.up()
    if ax == "X":
        pb = [a, 0]
        pe = [b, 0]
    else:
        pb = [0, a]
        pe = [0, b]
    tr.goto(pb)
    tr.down()
    tr.goto(pe)


def Mark(txy, ax="X"):
    a = txy[0]
    b = txy[1]
    tr.up()

    for t in range(a, b):
        if ax == "X":
            pb = [t, 0]
            pe = [t, 0.2]
            pw = [t, -0.5]
        else:
            pb = [0, t]
            pe = [0.2, t]
            pw = [0.2, t]
        tr.goto(pb)
        tr.down()
        tr.goto(pe)
        tr.up()
        tr.goto(pw)
        tr.write(str(t))


def Arrow(txy, ax="X"):
    a = [0.1, 0, -0.1]
    b = [-0.1, 0.3, -0.1]
    tr.up()
    tr.goto(0, 0)
    tr.begin_poly()

    for i in range(2):
        tr.goto(a[i], b[i])
    tr.end_poly()
    p = tr.get_poly()

    tr.register_shape("myArrow", p)
    tr.resizemode("myArrow")
    tr.shapesize(1, 2, 1)

    if ax == "X":
        tr.tiltangle(0)
        tr.goto(txy[1] + 0.2, 0)
        pw = [int(txy[1]), -1.0]
    else:
        tr.tiltangle(90)
        tr.goto(0, txy[1] + 0.2)
        pw = [0.2, int(txy[1])]
    tr.stamp()
    tr.goto(pw)
    tr.write(ax, font=("Arial", 14, "bold"))


def main():

    aX = [-15, 12]
    aY = [-5, 5]

    Dx = 800
    Dy = Dx / ((aX[1] - aX[0]) / (aY[1] - aY[0]))

    tr.setup(Dx, Dy)
    tr.reset()

    Nmax = 1000

    tr.setworldcoordinates(aX[0], aY[0], aX[1], aY[1])

    tr.title("Lab_8_2_1")
    tr.width(2)
    tr.color("blue", "blue")

    tr.ht()
    tr.tracer(0, 0)

    Axis(aX, "X")
    Mark(aX, "X")
    Arrow(aX, "X")

    Axis(aY, "Y")
    Mark(aY, "Y")
    Arrow(aY, "Y")

    tr.color("green")
    tr.width(3)
    dx = (aX[1] - aX[0]) / Nmax

    x = aX[0]
    y = Func(x)
    if y is None:
        tr.up()
        tr.goto(x, 0)
    else:
        tr.down()
        tr.goto(x, y)
    while x <= aX[1]:
        x = x + dx
        y = Func(x)
        if y is None:
            tr.up()
            continue
        else:
            tr.down()
            tr.goto(x, y)


if __name__ == "__main__":
    main()
tr.mainloop()

#N2

import turtle as tr
from random import uniform
from math import pow


def fun2_2(x, y):
    if (x < -8) or (x > 8):
        flag = 0  # False

    if (
        x <= 2
        and x >= -2
        and y <= 2
        and y >= -2
        and y < pow((x - 4), 2) + pow((y + 4), 2) - 4**2
        and x < pow((x + 4), 2) + pow((y - 4), 2) - 4**2
    ):
        flag = 1
    else:
        flag = 0
    return flag


aX = [-8, 8]  # левая и правая
aY = [-8, 8]  # нижняя и верхняя
Dx = 500
Dy = Dx / ((aX[1] - aX[0]) / (aY[1] - aY[0]))
tr.setup(Dx, Dy, 200, 200)
tr.reset()
Nmax = 10000

tr.setworldcoordinates(aX[0], aY[0], aX[1], aY[1])
tr.title("Lab_8_2_2")
tr.width(2)
tr.ht()
tr.tracer(0, 0)
tr.up()
mfun = 0  # точек попало в
# заштрихованную область
for n in range(Nmax):
    x = uniform(aX[0], aX[1])
    y = uniform(aY[0], aY[1])
    tr.goto(x, y)
    if fun2_2(x, y) != 0:  # попала
        tr.dot(3, "green")
        mfun += 1

    else:
        tr.dot(3, "#ffccff")
    tr.color("blue", "blue")
# Рисуем оси
# Ось X
tr.up()
tr.goto(aX[0], 0)
tr.down()
tr.goto(aX[1], 0)
# Ось Y
tr.up()
tr.goto(0, aY[1])
tr.down()
tr.goto(0, aY[0])

# координатные метки
# и надписи на оси X
tr.up()
for x in range(aX[0], aX[1]):
    tr.goto(x, 0.1)
    tr.down()

    tr.goto(x, 0)
    tr.up()
    tr.sety(-0.4)
    coords = str(x)
    tr.write(coords)
#
# на оси Y
for y in range(aY[0], aY[1]):
    tr.goto(0, y)
    tr.down()
    tr.goto(0.1, y)
    tr.up()
    tr.setx(0.2)
    coords = str(y)
    tr.write(coords)

poli = [0, 0.1, 0, -0.1, 0]
Arrbeg = int(aX[1])
Xpoli = [Arrbeg, Arrbeg - 0.1, Arrbeg + 0.3, Arrbeg - 0.1, Arrbeg]
tr.goto(Xpoli[0], poli[0])
tr.begin_fill()
tr.down()
for i in range(1, 5):
    tr.goto(Xpoli[i], poli[i])
tr.end_fill()

tr.up()
tr.goto(Arrbeg, -0.7)
tr.write("X", font=("Arial", 14, "bold"))

Arrbeg = int(aY[1])
Ypoli = [Arrbeg, Arrbeg - 0.1, Arrbeg + 0.3, Arrbeg - 0.1, Arrbeg]
tr.up()
tr.goto(poli[0], Ypoli[0])
tr.begin_fill()
tr.down()
for i in range(1, 5):
    tr.goto(poli[i], Ypoli[i])
tr.end_fill()

tr.up()
tr.goto(0.2, Arrbeg)
tr.write("Y", font=("Arial", 14, "bold"))
Sf = (aX[1] - aX[0]) * (aY[1] - aY[0]) * mfun / Nmax
tr.goto(1, 9)
fstr = "N = {0:8d}\nNf = {1:8d}\nSf = {2:8.2f}"
meseg = fstr.format(Nmax, mfun, Sf)
tr.write(meseg, font=("Arial", 12, "bold"))
print(meseg)
tr.mainloop()

