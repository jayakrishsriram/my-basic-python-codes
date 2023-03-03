n=int(input("Enter the number of row:"))
m=int(input("Enter the number of column:"))
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
e=matrix(n,m)
def addition():
    add=[]
    for r in range(n):
        p=[]
        for t in range(m):
            s=w[r][t]+e[r][t]
            p.append(s)
        add.append(p)
    for l in add:
        print(l)
addition()
