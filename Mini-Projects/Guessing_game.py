import random
print("===== NUMBER GUESSING GAME =====")
print("I'm thinking of a number between 1 and 100.")
game = (random.randint(1, 100))
count= 0
while True:
    guess = int(input("Guess the Number : "))
    count=count+1
    if guess > game:
        print(" Value is High ")

    elif guess < game:
        print("Value is Low ")
    elif guess == game:
        print(guess, "is 🎉 Correct! ")
        print("you guessed the number in",count,"attempts")
        break
    