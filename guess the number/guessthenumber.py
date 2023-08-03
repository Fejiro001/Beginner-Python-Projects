import random
# function for user to guess a random number
#generated by the computer
def guess(x):
    random_number = random.randint(1, x)
    # initialize guess
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Too low. Guess again')
        elif guess > random_number:
            print('Too high. Guess again')

    print(f'You have guessed the number {random_number} correctly')       

# function for computer to guess our correct number
def computer_guess(x):
    low = 1
    high = x
    message = ''

# c - correct
    while message != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could be high since low=high
        message = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
        if message == 'h':
            high = guess - 1
        elif message == 'l':
            low = guess + 1
    
    print(f"Computer guessed the number {guess} correctly!")

computer_guess(1000)