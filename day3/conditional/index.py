#conditional

#if condition:
    #do this
#else:
    #do this

#example
height = int(input("enter height "))

#bill ban đầu
bill = 0
#nhỏ hơn 120 thì được chạy, còn lớn hơn thì được chạy
if height > 120:
    print(f"ride is {height}")
    #kiểm tra thêm về tuổi
    age = int(input("nhập tuổi"))
    if(age >= 18):
        bill = 5
        print('trên 18 tuổi trả $7')
    elif 10 < age <18:
        bill = 7
        print('trả $5')
    if 45 <= age and age <= 55: #logical and
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 8
        print('còn non trả $3')

    want_photo = input("Do you wan take a photo")
    if want_photo == "Y":
        bill += 3
    print(f"Your final with money is ${bill}")

else: 
    print(f"can not ride because height is {height}")

# > - Greater than
# < - Less than
# >= - Greater than or equal to
# <= - Less than or equal to