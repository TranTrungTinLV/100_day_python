
# for i in range(1,10,3):
#     print(i)

#mutiple for loop
target_input = int(input("Enter number"))
# even_sum = 0
# for i in range(0,target_input + 1,2):
#     even_sum += i
#     print(i)
# print(even_sum)

alternative_number = 0

for i in range(1,target_input+1):
    if(i % 2 == 0):
        alternative_number += i
print(alternative_number)