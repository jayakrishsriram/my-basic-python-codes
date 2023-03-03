a=int(input('Enter Your Top 3 Marks in 10th:'))
b=int(input('Enter Your Top 3 Marks in 10th:'))
c=int(input('Enter Your Top 3 Marks in 10th:'))
print('Enter the theory mark for 11th ')
tamil=int(input('Enter Your Language Marks in 11th:'))
english=int(input('Enter Your English Marks in 11th  '))
maths=int(input('Enter Your Maths Marks in 11th:'))
physics=int(input('Enter Your Physics Marks in 11th:'))
chemistry=int(input('Enter Your Chemistry Marks in 11th:'))
computer=int(input('Enter Your Compputer Marks in 11th:'))
e=round((a+b+c)/6)
tamil=(tamil/90)*20
tam=tamil+e+30
print('Tamil Mark: ',round(tam))
english=(english/90)*20
eng=english+e+30
print('English Mark: ',round(eng))
maths=(maths/90)*20
mat=maths+e+30
print('Maths Mark: ',round(mat))
physics=(physics/70)*20
phy=physics+e+30
print('Physics Mark: ',round(phy))
chemistry=(chemistry/70)*20
che=chemistry+e+30
print('Chemistry Mark: ',round(che))
computer=(computer/70)*20
com=computer+e+30
print('Computer Mark: ',round(com))
print('Total mark',round(tam+eng+mat+phy+che+com))
phys=phy/2
chem=che/2
cut_off=mat+chem+phys
print('Cut off',round(cut_off,2))
