Person_Weight=float(input("Weight: "))
Person_Height=float(input("Height: "))
BMI=Person_Weight/Person_Height/(Person_Height*10000)
print("Your BMI is: ")
print(BMI)
if BMI>25 and BMI<30:
    print("You are overweight.")
elif BMI<25 and BMI>18.5:
    print("You are healthy.")
elif BMI<18 and BMI>1:
    print("You are underweight.")
