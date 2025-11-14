import random

guess = int(input('Enter your guess: '))
secret_num = random.randint(1, 10)
attempts = 0

while guess != secret_num:
    attempts += 1
    
    if guess > secret_num:
        print('too high - guess lower')
        guess = int(input('Enter your guess: '))
    elif guess < secret_num:
        print('too low - guess higher')
        guess = int(input('Enter your guess: '))
        
print(f'You guessed the number in {attempts} attempts')
