
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