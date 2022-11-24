print("Welcome to the pizza machine!!")

size = input("What is the size of the pizza you would like, S, M, L?")
pepperoni = input("Would you like pepperoni Y or N?")
cheese = input("Would you want extra cheese Y or N?")
bill = 0

if size == "S":
    bill = 15
    print("Small size has been chosen")

elif size == "M":
    bill = 20
    print("Medium size has been chosen")

else:
    bill = 25
    print("Large pizza has been chosen")

if pepperoni == "Y":
    if size == "S":
        bill += 2

    else:
        bill += 3

if cheese == "Y":
    bill += 1

print(f"Thank you for ordering! Your bill is ${bill}")