def f5():
  for i in range(516):
    a = bin(i)[2::1]
    if i % 2 == 0:
        a = a + '10'
    elif i % 2 != 0:
        a = '1' + a + '01'
    if int(a, 2) > 516:
        print(int(a, 2))
        break
    
