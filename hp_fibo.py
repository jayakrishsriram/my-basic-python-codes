print("Fibonacci Series")
n=int(input("Enter no. of Terms:"))
a=-1
b=1
s=0
for i in range(1,n+1):
    s=a+b
    print(s)
    (a,b)=(b,s)

