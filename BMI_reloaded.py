print("Welcome to the BMI Calculator")

h = float(input("Enter your height in meters please: "))
w= float(input("Enter your weight in kilos please: "))

bmi = w/h**2

print("Your BMI is: ",bmi)

if bmi <18.5:
    print("You are skinnyyyy")

elif bmi<25:
    print("Eh you normal")

elif bmi<30:
    print("ayo u overweight")

elif bmi<35:
    print("GODDAMN U FATT BOII")

else:
    print("OH SHIIIIIII-")