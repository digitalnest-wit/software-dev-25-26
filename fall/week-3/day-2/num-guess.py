import random

LOWER_BOUND = 1
UPPER_BOUND = 100

print(f'I\'m thinking of a number between {LOWER_BOUND} and {UPPER_BOUND}..')

secret_goal = random.randint(LOWER_BOUND, UPPER_BOUND)
attempts = 0
guess = int(input('Enter your guess: '))

while guess != secret_goal:
    if guess > secret_goal:
        print('Too high; try a smaller number.')
    else:
        print('Too low; try a larger number.')
    
    guess = int(input('Enter your guess: '))
    attempts += 1
        
print(f'\nYou got it! The secret number was {secret_goal}.')
print(f'It took you {attempts} attempts.')
