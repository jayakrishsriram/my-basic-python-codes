n=int(input("Enter the number of row of first matrix:"))
m=int(input("Enter the number of column of first matrix:"))
n2=int(input("Enter the number of row of second matrix:"))
m2=int(input("Enter the number of column of second matrix:"))
def matrix(n,m):
    a=[]
    for i in range(n):
        b=[]
        print("Enter the {}'st row".format(i+1))
        for j in range(m):
            c=int(input("Enter the {}'st element in that row:".format(j+1)))
            b.append(c)
        a.append(b)
    return(a)
print("1'st matrix")
w=matrix(n,m)
print("2'st matrix")
e=matrix(n2,m2)
def multi(w,e):
    mul=[]
    for r in range(len(w)):
        p=[]
        for t in range(len(e[0])):
            s=0
            for q in range(len(w[0])):
                s=s+w[r][q]*e[q][t]
            p.append(s)
        mul.append(p)
    for l in mul:
        print(l)
multi(w,e)        
try:
    pass
except exception:
    print("this matrix")
