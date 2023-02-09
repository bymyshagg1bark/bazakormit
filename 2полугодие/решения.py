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
            if y * 4 + 105 == z:
                print(z, y)
 def f14():
    a = '0123456789abcde'
    for x in a:
        f = int(f'123{x}5', 15) + int(f'1{x}233', 15)
        if f % 14 == 0:
            print(x, f // 14)
            break
def f15():
    for a in range(1, 100):
            if all(((x % 2 == 0) <= (x % 3 != 0)) or (x+a >= 100) for x in range(1, 100)):
                print(a)
                break
def oge():
  from itertools import product


for i in range(2,6):
    b = product('12',repeat = i)
    for n in b:
        a = 12
        for x in n:
            if x == '1':
                a -= 1
            else:
                a *= 7
        if a == 489:
            print(n)

def ma():
    k = 0
    for i in range(2, 10):
        b = product('12',repeat = i)
        for n in b:
            a = 1
            for x in n:
                if x == '1':
                    a += 1
                else:
                    a *= 2
            if a == 10:
                k += 1
    print(k)
def malch():
    k = 0
    for i in range(2, 25):
        b = product('12',repeat = i)
        for n in b:
            if n.count('2') > 1:continue
            a = 10
            for x in n:
                if x == '1':a += 1
                else: a *= 2
                if a == 17:break
            if a == 35:k += 1
    print(k)                     



