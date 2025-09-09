import random

computer = random.choice([1,2,3])

youstr = input("Enter : ")
youdict = {"r":1,"p":2,"s":3} # mene r,p,s ko ab 1,2,3 bana diya so now whatever
# will be done, it will be done with these 3 int
reversedict = {1:"rock",2:"paper",3:"scissor"} 

you = youdict[youstr]
# we have two numbers now computer which will be random and you which we will enter
# as r,p,s and it will be converted to 1,2,3 resp. internally

print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")      

if (you == computer):
    print("Draw")
else:
    if(you == 1 and computer == 2 ):
        print("You Lose")
    elif(you == 1 and computer == 3):
        print("You win")    
    elif(you == 2 and computer == 1):    
        print("You Win")
    elif(you == 2 and computer == 3):    
        print("You Lose")
    elif(you == 3 and computer == 1):    
        print("You Lose")
    elif(you == 3 and computer == 2):    
        print("You Win")
    else:
        print("Something Went Wrong")    
        

     


