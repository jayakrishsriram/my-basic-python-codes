import random
st,p,s='stone','paper','scissor'
a=[st,p,s]
win={(p,st),(s,p),(st,s)}
n=int(input("Enter the number of round:"))
b={1:st,2:p,3:s}
user=0
computer=0
def score():
    print("Player point:",user,"\nComputer point:",computer)
    if (user>computer):
        print("Hey you won the match in {} point".format(user-computer))
    elif(user==computer):
        print("Match Draw")
    else:
        print("Hey you lost the match just in {} point".format(computer-user))
for i in range(n):
    print("===================================================================")
    print("1-> stone\n2-> paper\n3-> scissor")
    c=int(input("Enter your choice:"))
    if c>=1 and c<=3:
        d=random.choice(a)
        print("Player choice:",b[c],"\nComputer choice:",d)
        if(b[c],d) in win:
            print("You won round {}.".format(i+1))
            user+=1
        elif b[c] in a and b[c]==d:
            print("Draw in round {}".format(i+1))
        else:
            print("You lost in round {}.".format(i+1))
            computer+=1
    else:
        print("invalid choice")
print("===================================================================")
score()        
                         
    
