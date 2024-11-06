import random

def guess_the_gem():
    print("Welcome to the simple guessing game!")
    name = input("Please input your name.\n")
    print("Nice to meet you",name, "hope you are feeling lucky!")
    print("There are 3 cups: Cup 1, Cup 2, Cup 3.")
    
    gem_location = random.randint(1, 3)
    
    try:
        user_guess = int(input("Guess which cup the gem is under (1, 2, or 3): "))
        if user_guess not in [1, 2, 3]:
            print("Please enter a number between 1 and 3.")
        elif user_guess == gem_location:
            print("Congratulations! You guessed correctly. The gem was under Cup", gem_location)
        else:
            print(f"Sorry, the gem was under Cup {gem_location}. Better luck next time!")
    except ValueError:
        print("Please enter a valid number (1, 2, or 3).")

guess_the_gem()
