# calculate your life in weeks using the mathematical operators and f-strings  

# tips, there are 365days in a year,  52 weeks in 1 year and 12 months in year

# write a program to calculate your life in weeks until you are 90

print("WELCOME TO THE NEW CHALLENGE");
year=input("Enter your current Years\n");
currentYear=int(year)
realYears=90-currentYear;

# now convert realYears to  weeks
YearsInWeeks=realYears*52;
yearsInMonths=realYears*12;
yearsInDays=realYears*365;

print(f"Your current year in weeks is {YearsInWeeks}, In months is {yearsInMonths} and in days is {yearsInDays}");