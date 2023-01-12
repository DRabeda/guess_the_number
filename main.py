import random
import time

print("Hey! You will play the guess the number game. Rules are simple. You have to enter", "\n",
"value which will represent range from which the number will be chose ", "\n", "and then you will have number of attempts to guess the right number")

time.sleep(5)

print("Please, input number") 

x = int(input())  #declare range 

r = range(x)  #transofrm int to range 


rand_num = (random.choice(r))

attempts = 3 if x < 10 else 5 if x < 20 else 10 if x < 40  else 50
print(attempts)

while attempts > 0: 
    guess_number= int(input('Guess the number! '))
    if guess_number == rand_num:
        print("Succes")
        break
    else:
        print("Please Try Again")
    attempts -= 1 
    print("you have " + str(attempts) + " left attempts")

if attempts==0: 
    raise ValueError("Too many attempts!")
    