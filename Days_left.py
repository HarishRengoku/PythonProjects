print("This program shall calculate how many years, months, days left till 90 years old: ")

age = int(input("Enter your age please: "))

years= 90 - age
months= 12*years
weeks=  52*years
days= 365*years

print(f"You have {years} years, {months} months {weeks} weeks and {days} days left my friend" )
print("You are a good person")