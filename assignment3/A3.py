import random

a = random.randint(1,10)
while True:
    b = int(input('Guess the number: '))
    if a == b:
        print('Correct')
        break
    elif b > a:
        print('Too High')
    elif b < a:
        print('Too Low')