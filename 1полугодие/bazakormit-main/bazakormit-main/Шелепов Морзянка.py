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
    
