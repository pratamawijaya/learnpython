class MyClass:
    data = "data inside class"

    def show(self):
        print("this is a message inside class")

myObj = MyClass()
myObjB = MyClass()

myObj.data = "change data"

print(myObj.data)
print(myObjB.data)
myObjB.show()