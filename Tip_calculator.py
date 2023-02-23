print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

num_of_split = int(input("How many people to split the bill? "))

tip_only= ((tip/100)*bill)/num_of_split
eat = bill/num_of_split

total = eat + tip_only

print(f"Each person needs to pay {round(total,2)}$ to cover the bill along with the tip. \nthe tip per person is {tip_only} and the bill per person is {eat}")
