def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    #Add code here to calculate BMI
    bmi = weight / (height * height)

    #Add code here to display calculate BMI
    print("BMI is " + str(bmi))

    #BMI range
    if bmi < 18.5:
        print("You Are Under Weight!")
    elif 18.5 <= bmi <= 25.0:
        print("You Are Normal Weight!")
    else:
        print("You Are Over Weight!")


calculate_bmi(weight=70, height=1.73)