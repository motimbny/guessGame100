#guessing game : user needs to guess a number between 0-100 and he has 5 strikes.
#if he fails a guess, he gets a hint.
#game is over when he ran out of lives or guess the right number
#written by Moti Ben Hamo
#A starting project to learn python language

import random

def hintnum(number,numhint,guess):
    if numhint==0:
        if number%2==0:
            s="Number is even"
        else:
            s="Number is not even"
    if numhint==1 or numhint>3:
        if number-guess>0:
            s="Number is greater then number guessed"
        else:
            s="Number is smaller then number guessed"
    if numhint==2:
        s="Difreence between Number and your guess is: "+ str(abs(number-guess))
    if numhint==3:
        if number//10==0:
         s="Number is between 0-10 "
        else:
            s="Number is greater then 10 "
    return s

if __name__ == '__main__':
    live=5  #number of strikes before game is over
    flag=True   #a flag to check if user guessed the number right
    hint=0    #to know what hint to show the user
    number=random.randrange(100)    #getting a random number 0-100
    while live>0 and flag:           #checks if game is still on
        guess=int(input("Guess the number : \n"))     #getting number from user
        if guess==number:
            flag=False           #change flag to false and letting the loop know game is over
        else:
            live-=1
            print("Your hint is : ",hintnum(number,hint,int(guess)))
            if live>0:
                print("\n you have : ",live," left")
            hint+=1

    if flag:                #checks if user won the game or ran out of lives
        print("Ran out of live :( \n")
        print("Good luck next time. number was : ",number)
    else:
        print("You did it!!! gread job!")
