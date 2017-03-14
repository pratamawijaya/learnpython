x = 3
print(x>3)
print(x==3)
print(x<5)


name = "Jack"
age = 25

if name == "Jack" and age == 25:
    print("Your name is %s, and your age %d" % (name,age))
if name == "Jack" or name == "Ricky":
    print("Your name is %s either your name is ricky" % (name))

if name in ["Jack","Cena","Ricky"]:
    print("Your name in our database")
'''
python doesn't have switch case condition
'''
x = 500
if x == 200:
    print("your number is 200")
elif x == 100:
    print("your number is 100")
else:
    print("neither all")