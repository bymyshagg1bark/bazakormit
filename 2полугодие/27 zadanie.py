with open('27_A.txt') as f:
    s = [x for x in f]
    s.pop(0)
    sp = []
    for i in s:
        sp.append(list(map(int, i.split())))
    for i in range(len(sp)):
        if sp[i][1] % 36 == 0:
            sp[i][1] = sp[i][1] // 36
        else:
            sp[i][1] = (sp[i][1] // 36) + 1
    print(sp) 
