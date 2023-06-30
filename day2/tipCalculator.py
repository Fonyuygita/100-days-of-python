# TIP CALCULATOR IN PYTHON
print("Welcome to the tip calculator");

bill=float(input("What was the total bill? $"));
tip=float(input("What percentage tip will you like  to giv? 10, 12, or 15  \n"));

numPeople=int(input("How many people will you like to split the bill? "));

# calculate the percentage tip

p=(tip/100)*bill;

# add it to the initial amount

totalTip=p+bill;
pTip=(bill/numPeople)*p
finalAnswer=round(pTip, 2);

print(f"Each person is suppose to pay {finalAnswer}$ ");
