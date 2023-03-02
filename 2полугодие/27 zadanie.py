with open('27_A.txt') as f:
    d = []
    s = [x for x in f]
    s.pop(0)
    for i in s:
        d.append(i.split())
