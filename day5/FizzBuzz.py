#Những số chia hết 3 là Fizz, chia hết 5 là Buzz và Chia Hết 3 với 5 là FizzBuzz

target_input = int(input("enter number"))
# alternative_number = 0
for i in range(1,target_input + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)