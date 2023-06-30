# BMI (body mass index) : way of measuring somebody's body composition independent from their height

print("Welcome to my BMI calculator___________");

weight=input("Enter your weight in kg: \n");
height=input("Enter your height in m: \n");


print("Your weight is " + weight + "kg " + " and your height " + " is " + height + "m");

print("Now lets calculate your Body mass index as follows_____________________");
# calculate the Bmi
# we  need to convert our strings above to numbers
bmi=float(weight) / float(height)**2;
bmi_convert=int(bmi);


print(f"Thank you for using our system, Your BMI is {bmi}kg/m^2\n");
