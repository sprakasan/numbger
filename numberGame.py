import random
number=random.randint(1,9)
print("Guess a number from 1 to 9.")
chance=0
while chance<5:
    guess=int(input("Enter your guess:"))
    if guess==number:
        print("Congrats! You guessed right!")
        break
    elif  guess<number:
        print("Your guess was too low, guess a number higher than ",guess)
    else:
        print("Your guess was too high, guess a number lower than ",guess)
    chance=chance+1

if not chance<5:
   print("You lost the game. The number was ",number)