k = 0
with open('26.txt') as f:
    s = [int(x) for x in f] 
    s.pop(0)
    s.sort(reverse = True)
    _min = s[0]
    for i in range(1, len(s)):
        if _min >= s[i] + 3:
            _min = s[i]
            k += 1
print(k + 1, _min)   
