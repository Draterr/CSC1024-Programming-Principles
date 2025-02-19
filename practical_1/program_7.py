total_bill = float(input("Enter The total bill: "))
no_of_friends = int(input("Enter The number of friends splitting the bill: "))

total_bill += total_bill*0.1
total_bill += total_bill*0.06
final = total_bill/no_of_friends
print(f"Each Friend has to pay {final:.2f}")
