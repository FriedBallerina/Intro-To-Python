import random

randomNumber = random.randint(0,10)
guess = int(input("guess a number!"))
while guess != randomNumber:
    if guess < randomNumber:
        print("aim higher!")
    else:
        print('aim lower!')
    guess = int(input("guess a number!"))
print('you guessed it, well done! the number was indeed', randomNumber)