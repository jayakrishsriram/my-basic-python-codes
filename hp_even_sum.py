print("Program to print the sum of even No\'s")
n=int(input('Enter a Number:'))
s=0
for i in range(2,n+1,2):
    s=s+i
print('Sum of even no.s 2...{} is {}'.format(n,s))

