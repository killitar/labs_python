#1
import math
# fx = open("laba_1","w")
fh = open("laba_1","r")
x = int(fh.read())
y = 1

if x >= -9 and x < -5:
    print("x = {0}, y = {1}".format(x, -math.sqrt(4 - (x + 7) ** 2) + 2))
elif x >= -5 and x < -4:
    print("x = {0}, y = {1}".format(x, 1))
elif x >= -4 and x < 0:
    print("x={0}, y = {1}".format(x, y / 2))
elif x >= 0 and x < math.pi:
    print("x={0}, y ={1}".format(x, math.sin(x)))
elif x >= math.pi and x <= 5:
    print("x={0}, y = {1}".format(x, x))
else:
    print("error")
# fx.close()
fh.close()

#2
import math

print("Введите координаты x,y,r")

fh = open("laba_2","r")
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
    print("Попадает")
else:
    print("Не попадает")
fh.close()
