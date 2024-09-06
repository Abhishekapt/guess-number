import random

def guessing_game(guessLimit, number):
    random_number = random.randint(1, number)
    try:
        while guessLimit > 0:
            guess = int(input('What is your guess? '))
            guessLimit -= 1
            if random_number == guess:
                print('Congrats, You got it right!')
                break
            elif guess < 1 or guess > number:  # Check if the guess is out of range
                print('Your guess is out of range')
            else:
                print('That was wrong.')
                
            print(f'You have {guessLimit} guesses left')
        
        print('Game Over')
        print(f'The random number was {random_number}')
    except ValueError:
        print('Only integers are allowed')

def easy():
    print('You have to guess a number between 1 and 10. You have 6 guesses.')
    guessing_game(6, 10)

def medium():
    print('You have to guess a number between 1 and 20. You have 4 guesses.')
    guessing_game(4, 20)

def hard():
    print('You have to guess a number between 1 and 50. You have 3 guesses.')
    guessing_game(3, 50)

def try_again():
    again = input('Do you want to play this game again? Yes/No: ')
    if again.upper() == 'YES':
        welcome()
    elif again.upper() == 'NO':
        print('Thanks for playing')
    else:
        print('Wrong input')
        try_again()
        
def welcome():
    print('Welcome to the guessing game!')
    difficulty = input('Choose your level: easy, medium, hard: ')
    if difficulty.upper() == 'EASY':
        easy()
        try_again()
    elif difficulty.upper() == 'MEDIUM':
        medium()
        try_again()
    elif difficulty.upper() == 'HARD':
        hard()
        try_again()
    else:
        print('This is wrong input')
        welcome()

welcome()
      