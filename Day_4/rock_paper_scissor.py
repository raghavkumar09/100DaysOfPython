import random

rock = ''' 
    _________
---'   (_____)_
        (______)
        (______)
        (______)
---.____(_____)

''' 

paper = '''
    ____________
---'      ______)_
          ________)
          ________)
          ________)
---.___________)

'''
scissor = '''

    ________
---'     ___)_______
         ___________)
         ___________)
        (______)
---.____(____)

''' 
game_images = [rock, paper, scissor]
user_choice = int(input("what do you choose? Type 0 for Rock , Type 1 for paper, Type 2 for scissor.\n")) 
print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer choice")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("you entered invalid number , you lose")
elif user_choice == 0 and computer_choice == 2:
    print("you win")
elif computer_choice == 0 and user_choice == 2:
    print("you lose")
elif user_choice == computer_choice:
    print("Draw")
elif computer_choice > user_choice:
    print("you lose")
elif user_choice > computer_choice:
    print("you win!")