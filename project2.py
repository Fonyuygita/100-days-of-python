# this projects focuses on understanding datatypes, type conversions and numbers 

# PROJECT NAME:TIP CALCULATOR

print(len("hello"));

# string 
# integer
# boolean
# 

    # 1 STRINGS
    # --subscripting
test="hello"[4];
print(test);   
# concatenation 
print("123" + "345");

# Integer datatype:numbers without any decimal places

print(123+345);

# float
3.14159
# boolean have two possible values true or false

# 3 TYPE ERROR, TYPE CHECKING, TYPE_CONVERSION
count=len(input("what is your name"));
print(count);
# to c heck type of data type inm python put in the type checking function
print(type(count));
# convert number into strings
convert=str(count);
print("you have converted your name count to " + convert + "characters");

print("EXERCISE 1");

choice=input("Enter a two digit number");  
strConvert=str(choice);
num1=int(strConvert[0]);
num2=int(strConvert[1]);
print(num1+num2);
