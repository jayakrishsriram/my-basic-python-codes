n=int(input('enter a Number:'))
sum=0
m=n
for i in range(1,4):
    sum=sum+m
    m=(10*m)+n
print('The sum is:',sum)
