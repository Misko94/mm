from random import randint
import sys


answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        print(answer)
        guess = int(input('guess a number 1-10: '))
        if guess > 0 and int(guess) < 11:
            if guess == answer:
                print('your are a genius!')
                break
        else:
            print('hey bozo, I said 1-10')
    except ValueError:
        print('please enter a number')
        continue
