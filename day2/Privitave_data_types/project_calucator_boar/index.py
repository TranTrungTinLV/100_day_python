print("Welcome to boa mát xa")

#If the bill was $150.00, split between 5 people, with 12% tip. 
total_bill = float(input("What was the total bill "))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15 "))
split_people = int(input("How many people to split the bill? "))

bill_with_tip = percentage / 100 # tiền tip

tip = bill_with_tip + 1


result = (total_bill / split_people) * tip
print(result)