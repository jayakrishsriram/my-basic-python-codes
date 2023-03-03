n=input("Enter")
a=[]
for i in range(len(n)):
        if(n[i]==','or n[i]=='\0'):
           continue
        else:
           a.append(n[i])    

print(a)        
        
