a=int(input())
if a<=1:
    print("Factorial is 1")
else:
    fact=1
    for i in range(1,a+1):
        fact*=i
    print(fact)