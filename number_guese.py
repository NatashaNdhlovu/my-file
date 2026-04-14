number = 50  # secret number
guesses = 0

print("I am thinking of a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    guesses += 1

    if guess < number:
        print("Too Low ")
    elif guess > number:
        print("Too High ")
    else:
        print("Correct ")
        print("You got it in", guesses, "guesses")
        break