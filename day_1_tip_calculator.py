#Tip calculator 

print("Welcome to the tip calculator")
total = float(input("What was the total bill?"))
procent = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))

bill_with_tip = procent / 100 * total + total
bill_per_person = bill_with_tip / people

bill_per_person_r = round(bill_per_person, 2)


print(f"Each person should pay: {bill_per_person_r}")
