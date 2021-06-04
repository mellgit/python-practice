# calculate BMI (bmi = weight / height2)

def main():
    print(bmi(110, 1.80))

def bmi(weight, height):
    val = weight/pow(height,2)
    if val <=18.5:
        return "Underweight"
    elif val <=25:
        return "Normal"
    elif val <=30:
        return "Overweight"
    else:
        return "Obese"


main()
"""
if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"

"""