import random
num = random.randint(1,5)

print(num)
for i in range(1, 6):
    guess = int(input('what is your guess?: '))
    if guess > num:
        print('your guess is to low')
    elif guess < num:
        print('your guess is to high')
    else:
        print('YOU GUESSED THE RIGHT NUMBER!')
        break
    
