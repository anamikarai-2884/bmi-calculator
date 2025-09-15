height=float(input("Enter your Hieght in cm: "))
weight=float(input("Enter your weight in kg:"))

height=height/100

BMI=weight/(height*height)

print("your Body mass index is:",BMI)

if BMI>0:

    if BMI<=16:
        Print("you are severely understanding")

    elif BMI<=18.5:    
        print("you are underweight")

    elif BMI<=25:
        print("you are healthy")

    elif BMI<=30:
        print("you are ovrerweight")

    else:
        print("you are severly overweight")
            
else:
    print("you have Entered invalid details!")
        