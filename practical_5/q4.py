while True:
    print("Temperature Conversion Programme.")
    print("[1] Convert Celsius to Fahrenheit.")
    print("[2] Convert Fahrenheit to Celsius.")
    selection = input("Enter your selection, 1 or 2: ")
    if selection == "1" or selection == "2":
        print("Celsius (C) to Fahrenheit (F) Conversion")
        print("Enter temperature in integer values only.")
        min_int = input("Enter minimum temperature: ")
        max_int = input("Enter maximum temperature: ")
        if min_int > max_int or min_int.isdigit() == False or max_int.isdigit() == False:
            print("ERROR: Invalid Input!")
        elif selection == '1':
            min_int = int(min_int)
            max_int = int(max_int)
            for i in range(min_int,max_int+1):
                fahrenheit = (i *9/5) + 32
                print(f"{i:>5}C = {fahrenheit:<5.2f}F")
            print("Conversion Done!")
        else:
            for i in range(min_int,max_int+1):
                celsius = (i - 32) * 5/9
                print(f"{i:>5}F = {celsius:<5.2f}C")
            print("Conversion Done!")
    else:
        print("ERROR: Invalid Selection!")
    run_again = input("Do you want to run the program again? [Y/N]: ")
    while run_again.upper() != "Y" and run_again.upper() != "N":
        run_again = input("Do you want to run the program again? [Y/N]: ")
    if run_again == "Y":
        continue
    else:
        break
