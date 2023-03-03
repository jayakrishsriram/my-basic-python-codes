
m=input('Enter a string:')
print("a - $")
n=''
for i in m:
    if i=='a':
        k='$'
        n+=k
    else:
        n+=i
print(n)
#==============
#m=input("Enter a string: ")
print("remove nth index")
n=int(input("Enter the index to be removed:"))
k=''
for i in range(len(m)):
    if i==n:
        continue
    else:
        k+=m[i]
print(k)
#===============
#m=input("Enter a string: ")
print("Replace First - Last")
k=''
j=m[len(m)-1]
for i in range(len(m)):
    if i==0:
        k+=j
    elif i==(len(m)-1):
        k+=m[0]
    else:
        k+=m[i]
print(k)
#===============
#m=input("Enter a string: ")
print("Count Lower")
k=0
for i in m:
    if i.islower():
        k+=1

print("count=",k)
#===============
#m=input("Enter a string: ")
print("Largest string")
k=0
n=input("Enter a string: ")
j=0
for i in m:
    k+=1
for i in n:
    j+=1

if j>k:
    print(n,"is Largest")
else:
    print(m,"is Largest")
#==============
#m=input("Enter a string: ")
print("Count Consonants")
s={'A','a','E','e','I','i','O','o','U','u'}
c=0
for i in m:
    if i not in s:
        c+=1

print("No. of Consonants:",c)

#==============
       
