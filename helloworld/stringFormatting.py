'''
%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)
'''

name = "John Cenna"
age = 30
print("%s is %d years old" % (name,age))

number = float(10000)
print("number is %.2f" % (number))