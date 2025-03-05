import random


while True:
    secret_num = random.randrange(100)
    guess_num = int(input('Guess my secret number: '))
    count = 1
    while guess_num != secret_num:
        if guess_num < secret_num:
            print("Too Low")
        else:
            print("Too High")
        count += 1
        guess_num = int(input('Have another guess: '))

    print('Well done, you took ' + str(count) + 'attempts')
    again = input("Do you want to play again? Type yes if so")
    if again.upper() != 'YES':
        break
    continue
