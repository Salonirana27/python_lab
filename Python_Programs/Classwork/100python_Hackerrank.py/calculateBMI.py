#calculate BMI category
weight = float(input("Enter your weight: "))
height = float(input("Enter your Height: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
    
    #output
    """Enter your weight: 50
Enter your Height: 54
Underweight
65
1.7
Normal weight

80
1.7
overweight
"""