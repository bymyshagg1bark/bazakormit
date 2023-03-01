k = 0
k_max = 0
with open('24.txt') as f:
    s = f.readline().replace('C','S').replace('D','S').replace('F','S')
    s = s.replace('A','G').replace('O','G')
    s = s.replace('SG','*')
    for i in range(len(s)):
        if s[i] == '*':
            k += 1
            k_max = max(k_max, k)
        else:
            k = 0
    print(k_max)