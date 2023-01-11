from math import log2

def znach():
    print('Введи значения, которые у тебя есть:I = 1,k = 2,3 = i, N = 4, 5-ввод закончен,6 - перейти к решению задачи')
    b = 1
    I = None
    k = None
    i = None
    N = None
    while b != 0:
        a = int(input('введи значение, которые у тебя есть'))
        match a:
            case 1:
                I = int(input('Введи I '))
            case 2:
                k = int(input('Введи k '))
            case 3:
                i = int(input('Введи i '))
            case 4:
                N = int(input('Введи N '))
            case 5:
                break
    print('Выбери переменную которую нужно найти: I - 1, k - 2, i - 3, N - 4, Закончить ввод - 5')
    while True:
        ch = int(input('введи номер переменной '))
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
                elif N is not None:
                    i = log2(N)
                    print(i)
                else:
                    print("Недостаточно данных для решения задачи!")
            case 4:
                if i is not None:
                    N = 2 ** i
                    print(N)
                else:
                    print('Недостаточно данных для решения задачи!')
            case 5:
                break


def zvuk():
    print(
        'Введи значения, которые у тебя есть: 1 = I(объем),2 = F(частота), 3 = i(глубина), 4 = t(время звучания),5 = k(моно или стерео')
    I = None
    F = None
    i = None
    t = None
    k = None
    while True:
        a = int(input('выбери перменные, которые нужно ввести'))
        match a:
            case 1:
                I = int(input('Введи I '))
            case 2:
                F = int(input('Введи F '))
            case 3:
                i = int(input('Введи i '))
            case 4:
                t = int(input('Введи t '))
            case 5:
                k = int(input('ВВеди k '))
            case 6:
                break
    a1 = int(input('введи, что хочешь найти 1 = I, 2 = F, 3 = i, 4 = t, 5 = k 6 = N'))
    match a1:
        case 1:
            if (F, i, t, k) is not None:
                I = F * i * t * k
                print(I)
            else:
                print('Недостаточно данных')
        case 2:
            if (I, i, t, k) is not None:
                F = I / (i * t * k)
            else:
                print('Недостаточно данных')

        case 3:
            if (F, t, k, I) is not None:
                i = I / (F * t * k)
                print(i)
            else:
                print('Недостаточно данных')
        case 4:
            if (I, F, i, k) is not None:
                t = I / (F * i * k)
                print(t)
            else:
                print('Недостаточно данных')
        case 5:
            if (I, F, i, t) is not None:
                k = I / (F * i * t)
                print(k)
            else:
                print('Недостаточно данных')
        case 6:
            if i is not None:
                N = 2 ** i
                print(N)
            else:
                print('Недостаточно данных')
def pic():
    ch = input('Что не известно? 1)K 2)b Неизвестно: ')
    if ch == '1':
        b = int(input('Введи b: '))
        print(f'k = {2 ** b}')
    elif ch == '2':
        K = int(input('Введи K: '))
        print(f'b = {log2(K)}')
a = int(input('Введи тип задачи, которую хочешь решить 1 - информация, 2 - звук, 3 - изображения'))
if a == 1:
    znach()
elif a == 2:
    zvuk()
elif a == 3:
    pic()
else:
    print('Такой функции нет')