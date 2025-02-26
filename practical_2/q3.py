income = float(input("Input yearly income: "))
tax = 0
if income >= 0 and income <= 2500:
    tax = income * 0 
elif income > 2500 and income <= 10000:
    tax = income *0.05
elif income > 10000 and income <= 50000:
    tax = income * 0.15
elif income > 50000:
    tax = income * 0.25
print(f"Tax: {tax}")
