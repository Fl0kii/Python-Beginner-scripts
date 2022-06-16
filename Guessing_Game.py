secret_word = "Enter secret word here"
guess = ""
guess_count = 0
guess_limit = 7
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
        if guess_count < guess_limit:
                guess = input("Guess the word ? \n")
                guess_count += 1
        else:
                out_of_guesses = True

if out_of_guesses:
        print("You lose!")
else:
        print("Winner!!")
