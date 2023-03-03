cost=0
a=True
while a:
       a=input("Do you want to buy any tickets \n Yes or No? ")
       if a=='no':
         print('Total cost',cost)
         a=False
       else: 
         age=int(input("Enter the age:"))
         if age<=3:
          cost=cost+0
         elif age>3 and age<=12:
           cost=cost+10
         else:
           cost=cost+15
          
