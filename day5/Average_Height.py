height_number = "156, 178, 165, 171, 187"

students_height = height_number.split(", ")
# print(students_height)

for i in range(0,len(students_height)):
    students_height[i] = int(students_height[i])
# print(students_height)


total_height = 0

for height in students_height:
    total_height += height
print(f"total height {total_height}")

#Chiều cao trung bình
number_student = 0

for height in students_height:
    number_student += 1
print("number height", number_student)

advantage_number_height = total_height / number_student

print(f'chiều cao trung bình {advantage_number_height}')