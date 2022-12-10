from math import *

fa = open("laba_1_a.txt","wt")
fh = open("laba_1.txt","rt")

a=float(fh.read()) 
z1 =(sin(2*a)+sin(5*a) - sin(3*a)) / (cos(a) + 1-2*(1-cos(2*a))) 
z2 = 2*sin(a) 

fa.write(str(z1)) 
fa.write('\n')
fa.write(str(z2))
fa.close()
fh.close()

#2
import math

print("Введите координаты x,y,r")

fh = open("laba_2","rt")
fa = open("laba_2_a","wt")
r = float(fh.readline())
x = float(fh.readline())
y = float(fh.readline())

if(
    x <= 2
    and x>=-2
    and y<=2
    and y>= -2
    and y>= math.pow((x-r),2) + pow((y+r),2)+r**2
    and x>=math.pow((x+r),2) + pow((y-r),2) +r**2
    
):
    fa.write("Попадает")
else:
    fa.write("Не попадает")
fh.close()
fh.close()

#3
from math import pow, factorial
 
print("Введите x_beg,x_end,d_x,eps")
 
fa = open("laba_2_a.txt","wt")
fh = open("laba_2.txt","rt")

xb = float(fh.readline())
xe = float(fh.readline())
dx = float(fh.readline())
eps = float(fh.readline())
 
xt = xb
 
fa.write("+---------+---------+---------+ \n")
fa.write("I    X    I    Y    I    N    I \n")
fa.write("+---------+---------+---------+ \n")
 
while xt <= xe:
    an = xt
    n = 0
    y = an
    while True:
        k = pow(xt, n) / factorial(n)
        an = an * k
        y += an
        n += 1
        if abs(an) < eps:
            break
    fa.write("I{0:7.2f}  I {1:7.3f} I{2:4f} I".format(xt, y, n))
    xt += dx
fa.write("\n+---------+---------+---------+")

