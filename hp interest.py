p=float(input('enter principle:'))
n=float(input('enter time:'))
r=float(input('enter rate:'))
s=(p*n*r)/100
c=p*((1+r/100)**n-1)
print('Simple Interest is: %f' %(s))
print('Compound Intrest is: %f' %(c))
