hourly_wage = float(input("Enter your hourly wage: "))
total_regular_hours = int(input("Enter your total_regular_hours: "))
total_overtime_hours = int(input("Enter your total_overtime_hours: "))

overtime_pay = (hourly_wage * 1.5) * total_overtime_hours
total_weekly_pay = hourly_wage * total_regular_hours + overtime_pay

print(f"Your weekly pay is {total_weekly_pay}")
