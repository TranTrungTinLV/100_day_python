name_string = "Angela, Ben, Levi, Micheal"
names = name_string.split(", ")
print(names) #array

num_items = len(names) #độ dài của mảng
print(num_items)
import random
random_choice = random.randint(0, num_items - 1) #random integer
print(random_choice)

print(f"{names[random_choice]} is going buy the meal today")
