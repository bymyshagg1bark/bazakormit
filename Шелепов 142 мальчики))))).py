def fam(x):
    print(x[::-1])


def chel(x,y):
    return x[::-1], y

def norm(x):
    g = {'а','о','у','е','ю','я','ы','ё','и'}
    k = 0

    for i in range(len(fam)):
        if fam[i] in g:
            print(fam[i])
fam = input('Введи фамилию ')

x = input('Введи фамилию ')
y = input('Введи пол ')
norm(x)
fam(x)
res = chel(x,y)    
print(res)