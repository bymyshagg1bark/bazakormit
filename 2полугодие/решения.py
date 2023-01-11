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
  from turtle import *
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

    
