day_of_the_week = 0

while True:
    day_of_the_week = int(input("Enter the day of the week: "))
    match day_of_the_week:
        case 1:
            print("Peppermint Mocha")
            continue
        case 2:
            print("Candy Bar Latte")
            continue
        case 3:
            print("Caramel Coffee")
            continue
        case 4:
            print("Chocolate Almond Cafe")
            continue
        case 5:
            print("Pumpkin-Chai Latte")
            continue
        case 6:
            print("Vanilla Chai Tea")
            continue
        case 7:
            print("Gingerbread Latte")
            continue
        case -1:
            print("exiting...")
            break
        case _:
            print("This day does not exist!")
            continue

