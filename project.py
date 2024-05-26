import random

def number():
    k=random.randint(1,50)
    while True:
        userinput=int(input("guess number between 1 to 50:"))
        if(userinput==k): 
            print("Congratulations! You did it :)")
            break
        elif(userinput<k):
            print("Number is bigger then your guess")  
        else:
            print("Number is smaller then you guess") 
        
        


while True:
    number()
    a=int(input("Press 1 for play again:"))
    if(a==1):
        print("Game start")
    else:
        print("Thanks for playing!")
        break  
