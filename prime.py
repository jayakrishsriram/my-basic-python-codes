a=int(input('no of input:'))
for i in range(a):
    b=int(input('Number:'))
    for j in range(1,b):
       e=b%j
       if e!=0:
          c='Not prime'
       if e==0:
          c='Prime'
    print(c)         
