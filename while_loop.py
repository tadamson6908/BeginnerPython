"""
Learn Conditional Repetion
For loops and while loops
"""


counter = 5
while counter:
    print(counter)
    #augmented operator
    counter -= 1

# Run forever
while True:
    print("Enter a number")
    response = input()
    if int(response) % 7 == 0:
        break




print("Done")