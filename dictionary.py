"""
Learn dictionaries
Dictionaries map keys to values

In some languages as associative arrays, hashes, or maps

Create them using {} containing a key value pair
retrieve them by [key value]
"""

d = {'alice': '801-123-45-8988',
     'pedro' : '956-445-78-8966',
     'john': '651-321-66-4477'}
print(d, type(d))
print(d['pedro'])

roster = {}
while True:
    name = input("Enter a name or quit to exit")
    if(name != "quit"):
        number = input("enter a grade")
        roster[name] = number
    else:
        break

print(roster)