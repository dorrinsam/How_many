import math

a = float(input())
b = float(input())
c = float(input())

if a == 0 and b != 0:
    print(1)
    exit()

#estesnaye aval
if a == 0 and b == 0 and c == 0:
    print('inf')
    exit()

#estesnaye dovom
if a == 0 and b == 0 and c != 0:
    print(0)
    exit()


delta = (b * b - 4 * a * c)

if delta < 0:
    print(0)
if delta == 0:
    print(1)
if delta > 0:
    print(2)











