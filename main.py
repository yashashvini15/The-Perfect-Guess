import random as r
number = r.randint(1,100)
guesses = 1
user_input = -1 
while(user_input !=number):
    user_input = int(input("Enter the guess : "))
    if(user_input > number):
        print("Go for lower number ")
        guesses+=1
    else:
        print("Go for higher number ")
        guesses+=1

print(f"You have guessed the {number} in {guesses}")