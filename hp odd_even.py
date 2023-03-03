a=input("Enter a Number:")
e=0
o=0
for i in range(0,len(a)):
    if (int(a[i])%2)==0:
        e+=1
    else:
        o+=1
print("%d odd digits , %d even digits"%(o,e))
