from random import randint
from time import sleep

# Generate answer
answer = randint(1,101)

#Print answer for debugging
print(answer)

# User interaction
username = input("Hi, there, What is your name?")
print(f"Hi, {username}! Please be my guest!!")

# Compare answer with user's guess
count = int(input("How much trials do you want?"))
point = 0

def compare_ans(an,usrname,coun,poin):
    if coun == 0:
        if poin == 0 :
            print('Your point is 0. you can get luck at another time')
        print("Sorry, the game is over.")
        return     
        
    else:
        # Get and print User's guess
        guess = int(input(f"So {username}, Guess the number(1-100) : "))
        print(f'Well choice {username}~~ You picked {guess}!!')
        
        if guess==an:
            print('************')
            sleep(1)
            print('************')
            sleep(1)
            print('************')
            sleep(1)
            poin += 1
            print(f'You got it right!! The answer is {an}!!')
            print(f"Your point is {poin}.")
            an = randint(1,101)  #assign new an
            print(an)   #Print answer for debugging
        elif guess>an:
            if coun == 1:
                print(f'Wrong answer! The answer was {an}, {usrname}!!')
            else:
                print(f'Keep going, man~! That is too high, {usrname}')
        elif guess<an:
            if coun == 1:
                print(f'Wrong answer! The answer was {an}, {usrname}!!')
            else:
                print(f'Keep going, man~! That is too low, {usrname}')

        coun -= 1
        compare_ans(an,usrname,coun,poin)

compare_ans(answer,username,count,point)

