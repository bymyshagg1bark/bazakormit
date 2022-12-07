import math
def znach():
  #  print('Введи значения, которые у тебя есть:I = 1,k = 2,3 = i, N = 4, 5-ввод закончен,6 - перейти к решению задачи')
    b = 1
    I = None
    k = None
    i = None
    N = None
    while b != 0:
        a = int(input('введи значение, нужные для решения задачи'))
        match a:
            case 1:
                I = int(input('Введи I'))
            case 2:
                k = int(input('Введи k'))
            case 3:
                i = int(input('Введи i'))
            case 4:
                N = int(input('Введи N'))
            case 5:
                break
   # print('I=', I, 'k=', k, 'i=', i, 'N=', N )
    print(k,i)
    print('Выбери переменную которую нужно найти: I - 1, k - 2, i - 3, N - 4')
    ch = int(input('введи номер переменной'))
    match ch:
        case 1:
            if k is not None and i is not None:
                I = k * i
                print(I)
            else:
                print("Недостаточно данных для решения задачи!")
        case 2:
            if I is not None and i is not None:
                k = I / i
                print(k)
            else:
                print("Недостаточно данных для решения задачи!")
        case 3:
            if I is not None and k is not None:
                i = I / k
                print(i)
            elif I is not None and k is not None:
                i = math.log2(M)

            else:
                print("Недостаточно данных для решения задачи!")








znach()