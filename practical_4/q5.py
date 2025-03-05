secret_num = 50
guess = 0
i = 0
while True:
    guess = int(input("Enter your guess: "))
    i+=1
    if guess > secret_num:
        print("Your guess is too high")
    elif guess < secret_num:
        print("Your guess is too Low")
    else:
        break

print(f"Well done you took {i} attempts")
