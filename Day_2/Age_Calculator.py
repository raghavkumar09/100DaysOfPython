
# creat a program using f-string to find how many days ,weeks,months form age input.

age = input("Enter your age : ")
age_as_int = int(age)

remaining_year = 90 - age_as_int
remaining_days = remaining_year * 365
remaining_weeks = remaining_year * 52
remaining_months = remaining_year * 12

Calculation =f"your days is {remaining_days}, your weeks is {remaining_weeks}, your months is {remaining_months}"
print(Calculation)
