student_score = [78,65,12,1,4,19,28]

for i in range(0,len(student_score)):
    student_score[i] = int(student_score[i])
print(student_score)

hightest_score = 0

for score in student_score:
    if score > hightest_score:
        hightest_score = score
print(hightest_score)