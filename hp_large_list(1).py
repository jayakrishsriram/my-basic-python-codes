n=[14,23,34,45,56,66,43,25,39,99,57]

def s_largest():
    for k in range(0,len(n)-1):
        for i in range(0,len(n)-1):
            for j in range(0,i+1):
                if n[j]>n[j+1]:
                    (n[j],n[j+1])=(n[j+1],n[j])
                
    
print("N=",n)
s_largest()
print("N =",n)

