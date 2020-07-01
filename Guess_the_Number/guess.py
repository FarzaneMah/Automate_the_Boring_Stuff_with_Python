#GUESS number game
import random as rd
name = input('What is your name?')
secret_number = rd.randint(1,100)
print(name , 'I am thinking of a number between 1, 100.')
for guess_Taken in range(1,8):
    guess = int(input('Take a geuss?'))
    if  guess < secret_number:
        print('Your guess is too low')
    elif  guess > secret_number:
        print('Your guess is too high')
    else:
        break
if guess == secret_number:
    print('Wow, ', name, '! Correct!')
else:
    print('Nope, ', 'The number I was thinking of was', secret_number)
