import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, Type 1 for paper or Type 2 for scissors"))

computer_choice = [rock, paper, scissors]

number_index = len(computer_choice)

random_choice_computer = random.randint(0,int(number_index) -1) #using

if user_choice >= 3 or user_choice <= 0:
    print("You lose it not exist")
elif user_choice == random_choice_computer: 
    print("You Win")
    print(f"user_choice \n {computer_choice[user_choice]}")
    print(f"computer_choice \n {computer_choice[random_choice_computer]}")
else:
    print("You lose")
    print(f"user_choice \n {computer_choice[user_choice]}")
    print(f"computer_choice \n {computer_choice[random_choice_computer]}")



