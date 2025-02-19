data_usage = float(input("Enter your daily data usage: "))
excess = 0
total_cost = 0
if data_usage <= 10:
    total_cost = data_usage * 15
else:
    excess = data_usage - 10
    total_cost = (excess * 30) + (10 * 15)

print("Your total cost is",round(total_cost,2))
