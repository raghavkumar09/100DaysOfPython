# Write a program to interprets the BODY MASS INDEX based on user input

print("Body Mass Index Calculater")

height = float(input("Enetr your height : "))
weight = float(input("Enetr your weight : "))
calculate_bmi = (weight / height**2)
BMI = round(calculate_bmi,2)
print(BMI)

if BMI < 18.5:
    print(f"your BMI is {BMI}, You are underweight")
elif 18.5 < BMI < 25:
    print(f"your BMI is {BMI},Normal weight")
elif 25 < BMI < 30:
    print(f"your BMI is {BMI}, you are overweight")
elif 30 < BMI < 35:
    print(f"your BMI is {BMI}, you are obese")
else:
    print(f"your BMI is {BMI}, you are clinically obese")