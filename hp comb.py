def comb(l):
    for i in range(4):
        for j in range(4):
            for k in range(3):
                for h in range(4):
                    if(i!=j and j!=k and k!=i and h!=i and h!=j and h!=k):
                        print(l[i],l[j],l[k],l[h])

a=input('Enter a 4 digit Number: ')
comb(a)
    
