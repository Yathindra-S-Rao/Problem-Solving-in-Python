# Monthly Expenses

expense_dict = {
    "Home Rent": None,
    "Electricity": None,
    "Water": None,
    "Cable": None,
    "Act": None,
    "Other": None
}

sharing_percentage_dict = {
    "Home Rent": 0.33,
    "Electricity": 0.33,
    "Water": 0.33,
    "Cable": 0.33,
    "Act": None,
    "Other": 0.33
}

for exp in expense_dict:
    expense_dict[exp] = float(input("Enter the expense [ " + exp + " ] : "))

print(expense_dict)

print("Expense_Report")
print("=====================")
print("Viji's")
