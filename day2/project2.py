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

    #   mathematical operation in python 
    # 1+2;
    # 2-4
    # 3*6;
    # 4/2 returns a float when you have divison
    # 3 ** 4  3 raised to the power 4
    #  mathematician lovees python because it is highly optimized for maths
    # PEMDASLR (Parenthesis, Exponents, multiplication, division, addition, subtraction); (), **, */, +  (FROM LEFT TO RIGHT)
    
print(3 * 3 + 3 / 3 - 3);
# In other to print 3 we hahve the following'

print(3*(3+3)/3-3); 
    
    