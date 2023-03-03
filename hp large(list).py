n=[14,23,34,45,56,66,43,25,39,99,57]

def largest():
    l=n[0]
    d=[]
    for i in range(0,len(n)):
        if n[i]>l:
            l=n[i]
            d.append(n[i])
            print(d)
            a=i
    print("d[",len(d)-2,"]",d[len(d)-2])
largest()                    
            
