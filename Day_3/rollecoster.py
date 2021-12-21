
print("Welcome TO Rollercoster")
height = int(input("Enter your height in cm : "))
bill = 0
if height >= 120:
    print("you can ride rollercoster")
    age = int(input("Enter your age : "))
    if age < 12:
        bill = 5
        print("child ticket are 5$")
    elif age <= 18:
        bill = 7
        print("youth ticket are 7$")
    else:
        bill = 12
        print("Adult ticket are 12$")

    want_photo = input("Do you want to photo taken y and n : ")
    if want_photo == "y":
        bill += 3

        print(f"your finall bill is {bill}")
else:
    print("Sorry, you can grew taller then come here")