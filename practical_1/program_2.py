amount = float(input("Enter an RM amount to be converted to SGD: "))

exchange_rate = 1/3.04
converted = amount * exchange_rate
print(f"That's {converted:.2f} in SGD")
