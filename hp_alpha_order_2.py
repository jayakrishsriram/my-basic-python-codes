n=input("Enter a string: ")
n=n.lower()
o=[]
for i in n:
    o+=i
print(o)
for k in range(0,len(o)-1):
    for i in range(0,len(o)-1):
        for j in range(0,i+1):
            if o[j]>o[j+1]:
                (o[j],o[j+1])=(o[j+1],o[j])

print(o)

'''
for i in ragne(len(o)):
    if

                
    
print(m)
'''

