from itertools import product
from turtle import *

def f5():
  for i in range(516):
    a = bin(i)[2::1]
    if i % 2 == 0:
        a = a + '10'
    elif i % 2 != 0:
        a = '1' + a + '01'
    if int(a, 2) > 516:
        print(int(i))
        break
        
def f6():
  
left(90)
for i in range(7):
    forward(300)
    right(120)
pu()
for x in range(1,9):
    for y in range(1,10):
        goto(x*30,y*30)
        dot(2)
done()

def f8():
    nums = product('01234567', repeat = 5)
    k = 0
    n = '16 36 56 76 61 63 65 67'
    nn = n.split()
    for n in nums:
        numb = ' '.join(n)
        sp = []
        if numb.count('6') == 1 and numb[0] != '0':
            for x in nn:
                if x in numb:
                    sp.append(x)
            if not sp:
                k += 1
    print(k)
def f12():
    sp =[]
    for i in range(2, 1000):
        n = 0
        for x in range(2, i):
            if  i % x  == 0:
                n += 1
        if n == 0:
            sp.append(i)
    print(sp)
    for z in sp:
        for y in range(100):
            if y * 4 + 117 == z:
                print(y, i)
    
