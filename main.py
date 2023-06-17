import random

print("==============================================================")
print("\t\tNUMBER GUESSING GAME\n\n")
print("==============================================================")
name = input("enter you name: ")
print("\n\n \t HELLO ", name," SO HERE ARE SOME RULES YOU SHOULD KNOW BEFORE STARTING\n\n")
print("1. I WOULD THINK A RANDOM NUMBER IN MY MIND AND YOU WOULD HAVE TO GUESS\n")
print("2. MY ASSUMED NUMBER WILL BE 0 TO 100 INCLUSIVE\n")
print("3. YOU WOULD HAVE A TOTAL OF 10 ATTEMPTS TO GUESS MY NUMBER\n\n")

x=True

while(x):
    win = 0
    wrongguess = 0
    mynum = random.randint(0,100)
    print("threee....twwoooo....one.....\n\n guess the number i have generated for you\n\n")
    while(wrongguess<10 and win!=1):
        guessednum = int(input("enter your guess: "))
        print("\n\n")
        if(mynum==guessednum):
            win=1
            print("\tWHAT A GUESS ", name ," !!! congratulations on your win you won the game in just ",wrongguess,"guesses\n\n")
            break
        elif (mynum != guessednum):
            wrongguess += 1
            print("\t\tohhh noo wrong guesss ")
            if(mynum>guessednum):
                closeness = mynum - guessednum
            elif(guessednum>mynum):
                closeness = (mynum - guessednum)*(-1)
            if (closeness<=10):
                print (name , "you are very close to my assumed number!!!")
            elif(closeness<=20):
                print(name , "brain storm a little more")
            else:
                print ("oh no! thats too far away from it!!")

    if(win == 0):
        print("oopssss!!! the number i generated was", mynum, ":(( \n")

    again = int(input("DO YOU WANT TO PLAY AGAIN?? ENTER 1 FOR A GO AGAIN..."))
    if(again == 1):
        x=1
    else:
        x=0
    
       
    

     
