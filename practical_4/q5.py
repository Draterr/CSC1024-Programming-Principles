secret_num = 50
guess = 0
i = 0
while True:
    guess = int(input("Enter your guess: "))
    if guess != secret_num:
        print("Your guess is too low or too high")
        i+=1
    else:
        break

print(f"Well done you took {i} attempts")
