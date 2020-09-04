x1 = int(input('Input x1:'))
y1 = int(input('Input y1:'))
x2 = int(input('Input x2:'))
y2 = int(input('Input y2:'))
x, y = 4, 4

k = (x2-x1)/(y2-y1)
b = y1-k*x1

if y == (k*x +b):
    print('Point on a line')
if y > (k*x+b):
    print('Point above')
if y < (k*x+b):
    print('Point below')