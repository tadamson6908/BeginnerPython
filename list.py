"""
Learn about lists
unlike strings, lists are mutable
You can update and append elements to it

"""
l = [1,2,3]
print("List ", l, type(l))

# A list of objects(any type)
a= ["apple", "orange", "pear"]
# Access by index notation
print(a, a[1])
#replace an element
a[0] = "tomatoes"
print(a, a[1])
a[1] = 3.14
print(a, a[1])
names = []
print("Enter three names:")
counter = 0
while counter != 3:
    names.append(input("Enter name: "))
    counter += 1

print(names)