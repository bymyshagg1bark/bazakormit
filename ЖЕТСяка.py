def morz():
    a = 'abcedfghiijklmnopqrstuvwxyz'
    abc = list(a)
    print(a)    
    b = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. .---- ..---  ...-- ....- ..... -.... --... ---.. ----. -----'
    abcm = b.split()
    print(abcm)
        
    text = input('vvedite text na angliyskom ')
    indm = ' '
    for i in range(len(text)):
        ind = abc.index(text[i])
        indm = indm + abcm[ind]
    print(f'{indm}')

def des():
    print('Введи основание системы p=')
    p=int(input())
    print('Введи исходное число')
    Np=int(input())
    k=int(1)
    N10=0
    while not Np==0:
        N10=N10+(Np%10)*k
        k=k*p
        Np=Np//10
    print('N10=', N10)

def ades():
    x=int(input("vvedi chislo"))
    a=list(str(x))
    print(a)
    y=int(input("vvedi stepen"))
    st=len(a)-1
    itog=int()

    for i in range(st+1): 
        itog=itog+(int(a[i])*(y**st))
        st=st-1

    print(itog)

def tabl():
    p = int(input('Введите p (2<p<=10): '))
    print (f'{p}-ичная таблица умножения')
    for x in range (1,p):
        for y in range (1,p):
            z = (x*y // p)*10+(x*y)%p
            print (z, end = ' ')
        print ()
    

def hem():
    a='0123456789'
    nums=list(a)
    print(nums)
    b='0000000 0001111 0010110 0011001 000101 0101010 0110011 0111100 1000011 1001100'
    hem=b.split()
    print(hem)
    for i in range(len(hem)):
        hem[i]=int(hem[i])
        print(hem)

    def distance(x,y):
        k=7
        for i in range(7):
            if x%10==y%10:
                k=k-1
            x=x//10
            y=y//10
        return k    
    cod=int(input("код"))
    min=distance(cod,hem[0])
    imin=0
    for i in range(10):
        D=distance(cod,hem[i])
        if D<min:
            min=D
            imin=i
    if min==0:
        print(f"код верный: символ {nums[imin]}")
    elif min==1:
        print(f"код исправлен: символ {nums[imin]}")
    else:
        print("Код неверный")

baza = int(input('Выбери программу \n1 - морзянка, \n2 - перевод в десятичную, \n3 -перевод в систему счисления, \n4 - таблица умножеия, \n5 - хеминг \n'))
match baza:
    case 1:
        morz()
    case 2:
        des()
    case 3:
        ades()
    case 4:
        tabl()
    case 5:
        hem()
    