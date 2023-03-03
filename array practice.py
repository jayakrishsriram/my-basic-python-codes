from array import *
'''a=array('i',[2,4,5,67,8,121])
print(a.typecode)
print(a)
for i in a:
    print(i,end='\t')
'''
a=array('i',[])
b=int(input('Enter the Number of Inputs in this array: '))
for i in range(b):
    c=int(input('Enter the 1st/Next array value: '))
    a.append(c)
print(a)            
for j in a:
    print(j)
d=int(input('Enter the array value to be found: '))
e=0
for k in a:
    if k==d:
        print('Index Value is',e)
        break
    e+=1
else:
    print('Not found')
