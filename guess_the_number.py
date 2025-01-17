import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'



def configure_range():
    """ Set the high and low values for the random number """
    return 1, 10


def generate_secret(low, high):
    """ Generate a secret number for the user to guess """
    return random.randint(low, high)

def increment_guess_counter(total_guesses):
    """Increments the total guesses for each successive loop"""
    total_guesses += 1
    return total_guesses

def get_guess():
    """ get user's guess, as an integer number """
    
    while True:
        try:
            number_2 = int(input('Please enter an integer number. You have as many tries as you need to enter a number: '))
            # if the user enters a number, it will be stored in the variable
            # number and your program can use it.
            print(f'Thank you for entering the number {number_2}')
            break   # we have a number, no need to repeat the loop
        except ValueError:
            # if the user doesn't enter a number, the line with int() in raises
            # A ValueError exception and then this block of code will run.
            print('That was not an integer number. Try again.')
            # since we are in a while True loop, the loop will repeat and ask the user for input again.
    return number_2

def check_guess(guess, secret):
    """ compare guess and secret, return string describing result of comparison """
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():
    total_guesses = 0
    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        total_guesses = increment_guess_counter(total_guesses)
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)

        if result == correct:
            break

    print(f"It took you {total_guesses} guesses this time.")
    print('Thanks for playing the game!')


if __name__ == '__main__':
    main()
