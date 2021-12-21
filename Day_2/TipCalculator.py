print("*****Tip Calculator******")

bill_amount = float(input("What was the total bill in $ "))
tip = int(input("What pracntage would like to give? 12 ,15 ,10? "))

people = int(input("How many people to split the bill? "))

tip_as_percentage = tip/100
total_tip_amount = tip_as_percentage * bill_amount
total_bill = bill_amount + total_tip_amount
bill_per_person = total_bill / people

final_result = round(bill_per_person,2)

print(f"Each person should pay {final_result} ")
