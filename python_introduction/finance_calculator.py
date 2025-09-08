#calculation of monthly income and rest
monthly_income = int(input("Enter your monthly income"))
monthly_expenses = int(input("Enter your montly epenses"))
monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print (f"Projected Savings after one year,with interest, is : {projected_savings}")
