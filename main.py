# Get values from console
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# convert values to float type
heightint = float(height)
weightint = float(weight)

# calculate BMI
BMI =  weightint / (heightint ** 2)

# print BMI
print("your BMI is : " + str(BMI))








