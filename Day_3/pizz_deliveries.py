# Q. To write a program to create Automatic pizza order program

# Based on user's input
# 1.pizza size
#     1. small pizza price = $15
#     2. medium pizza price = $ 20
#     3. large pizza price = $ 25
# 2.paperoni
#     1. samll paperoni = $2
#     2. large or medium paperoni = $3
# 3. chease for any size = $1


print("Welcome to pizz deliveries")

pizza_size = input("Enter your pizz size L , M , S : ")
add_paperoni = input("Do you want to paperoni Y , N : ")
add_cheese = input("Do you want to add extra cheese Y , N : ")
price = 0

if pizza_size == "S":
    price += 15
elif pizza_size == "M":
    price += 20
elif pizza_size == "L":
    price += 25
else:
    print("Something Wrong")

if add_paperoni == "Y":
    if add_paperoni == "S":
        price += 2
    else:
        price += 3
else:
    print("Try again")

if add_cheese == "Y":
    price += 1

print(f"Total price is {price}")
