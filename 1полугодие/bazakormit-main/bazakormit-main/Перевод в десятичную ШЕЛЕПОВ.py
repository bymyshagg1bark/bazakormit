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