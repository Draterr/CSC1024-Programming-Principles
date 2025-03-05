number = 0
while True:
    user_iunput = input("Enter a number: ")
    if user_iunput.upper() == "DONE":
        print("Ending ...")
        break
    number += int(user_iunput)
    print(number)
    
