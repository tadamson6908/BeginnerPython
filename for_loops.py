"""
Practice for loops
Keyword: for
"""

cities = ["london", "New York" , "Madrid", "Paris", "Ogden"]
for city in cities:
    print(city)

d = {'alice': '801-123-45-8988',
     'pedro' : '956-445-78-8966',
     'john': '651-321-66-4477'}

for item in d:
    print(item, "=>", d[item])