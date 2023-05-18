with open("24-241.txt") as f:
    sp = []
    s = f.readline()
    s = s.split('E')
    for i in s:
        if i.count('B') == 2  and i.count('A') > 5:
            nachalo_B = i.find('B') 
            konec_B = i.rfind('B')
            nachalo_A = i.find('A')
            konec_A = i.rfind('A')
            if nachalo_B < nachalo_A and konec_B > konec_A:
                sp.append(len(i))
    print(min(sp))


    
