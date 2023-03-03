per=[]
while True:
    Na=input("Enter a Name: ")
    age=int(input("Enter Age: "))
    per.append([Na,age])
    ch=input("Continue [y/n] ??")
    
    if ch in ('n','N'):
        break
    
print("Sno\t Name\t\t Age\t Eligible Status")
l=len(per)
for i in range(0,l):
    if per[i][1]>=18:
        print("{}\t {}\t\t {}\t Eligible\t".format(i+1,per[i][0],per[i][1]))
    else:
        print("{}\t {}\t\t {}\t Not Eligible\t".format(i+1,per[i][0],per[i][1]))
