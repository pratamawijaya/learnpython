'''
A dictionary is a data type similar to arrays, 
but works with keys and values instead of indexes. 
Each value stored in a dictionary can be accessed using a key,
which is any type of object (a string, a number, a list, etc.) 
instead of using its index to address it.
'''

phonebook = {}
phonebook["john"] = 12353646
phonebook["chena"] = 24215235

print(phonebook)

phonebooks = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebooks)

# iterating data from dict and print them
for name, number in phonebooks.items():
    print("Phone number of %s is %d" % (name,number))