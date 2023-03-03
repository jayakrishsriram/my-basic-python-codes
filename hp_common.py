a=set(input("Enter a string: "))
b=set(input("Enter a string: "))
c=a.intersection(b)
print(c)
a=a-c
b=b-c
d=len(a.union(b))
f="FLAMES"
fs=set("FLAMES")
n=0
while(len(fs)!=1):
    for j in f:
        n+=1
        if n==d:
            fs.discard(j)
            n=0
            f=str(fs)
print(fs)
            
    



            
