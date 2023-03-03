air=['Jai','Krish','Ram']
for i in air :
    print(i+'!'+' You are invited to the party.')
a=air.pop(2)
print('\n'+a+' is unable to attend the party \n')
air.insert(2,'Raj')
for i in air :
    print(i+'!'+' You are invited to the party.')
print('\n Hey Guys! we found  big table \n')    
air.insert(1,'Raja')
air.insert(0,'Ravi')
air.append('Sam')
for i in air :
    print(i+'!'+' You are invited to the party.')
