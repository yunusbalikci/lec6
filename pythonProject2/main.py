
he = int(input("What is your height?"))
we = int(input("What is your weight?"))

bmi = we / (he * he)

print("The BMI is", format(bmi), "so ", end='')

if (bmi < 16.0):
    print("Starvation")

elif (bmi >= 16.0 and bmi < 16.99):
    print("Emaciation")

elif (bmi >= 17.0 and bmi < 18.49):
    print("Underweight")

elif (bmi >= 18.50 and bmi < 24.99):
    print("Correct Weight")

elif (bmi >= 25.0 and bmi < 29.99):
    print("Overweight")

elif (bmi >= 30.0 and bmi < 34.99):
    print("First degree obesity")

elif (bmi >= 35.0 and bmi < 35.99):
    print("Second degree obesity")

else:
    if bmi < 40.0:
        print("Third degree obesity")
        pass

print("Your BMI is : ",format(bmi))

