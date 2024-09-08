""" Guessing Game """
'''
Simple Question ->
* choosing any number
* set guess count and guess limit
* then run while loop with correct condition with 'input from the user'
* set if statement inside the while loop
* and print the output
'''

secret_number = 10
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You win!")
        break
else:
    print("Sorry, You guess wrong!")