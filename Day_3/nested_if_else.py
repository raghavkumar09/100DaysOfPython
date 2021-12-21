
# Q. ROller coster 

print("Welcome TO Rollercoster")

height = int(input("Enter your height in cm : "))
if height >= 120:
    print("you can ride rollercoster")
    age = int(input("Enter your age : "))
    if age <= 18:
        print("please pay 7$")
    else:
        print("please pay 12$")
else:
    print("Sorry, you can grew taller then come here")