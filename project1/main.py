import random

'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice:")
youDict = {"s":1, "w":-1, "g":0}
reverseDict ={1:"Snake", -1:"Water", 0:"Gun"}

you = youDict[youstr] # converting into dictionary

# by now we have 2 numbers (variables) , you and computer

print(f"you chose: {reverseDict[you]}\nComputer chose: {reverseDict[computer]}")

if(computer==you):
    print("It is a draw!")
else:

    if(computer==-1 and you==1): # -2
        print("You won!")
       

    elif(computer==1 and you==-1): # 2  *
        print("You lost!")

    elif(computer==0 and you==-1): # -1
        print("You won!")
        


    elif(computer==-1 and you==0): # -1 *
        print("You lost!")

    elif(computer==1 and you==0): # 1
        print("You won!")
        


    elif(computer==0 and you==1): # -1 *
        print("You lost!")

    else:
        print("Something went wrong!")


# if((computer-you)==-1 and (computer-you)==2):
#     print("You lost!")
# else:
#     print("You")