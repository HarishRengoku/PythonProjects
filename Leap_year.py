print("Welcome to the leap year checker: ")

year= int(input("Enter your year: "))

a = year % 4
b = year % 100
c = year % 400

if a == 0:
    if b == 0:
        if c == 0:
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
        print("It is a leap year")
else:
    print("It is not a leap year")
