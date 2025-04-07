import random

def play_game():
    secret_number = random.randint(1,10)
    print("i'm thinking of a number between 1 and 10. can you guess it?: ")

    while True:
        try:
            guess =  int(input("enter your guess: "))
            match guess:
                case _ if guess == secret_number:
                    print("congratulations, you guessed it!")
                    break 
                case _ if guess > secret_number:
                    print("oops, your guess is a bit high. try again!")
                case _ if guess < secret_number:
                    print("nope, your guess is too low. give it another trial!")
        except ValueError:
            print("please enter a valid number.")

play_game()

play_again = input("so you want to play again? (yes/no): ")
if play_again == "yes":
    play_game()
else:
    print("thanks for playing! goodbye.")

play_game
