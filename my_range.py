"""
Learn about range() collection
"""




def main():
    """
    Test function
    :return:
    """
    for i in range(5):
        print(i)
    print("Starting at 5")
    for i in range (5,10):
        print(i)
    l = list(range(5,10))
    l2 = (list(range(5,10)) + list(range(30,40)))
    print(l)
    print(l2)

    l3 = list(range(0, 20, 2))
    print(l3)


    s = [0,2,3,4,6]
    for i in range(len(s)):
        print(s[i])

    t = [6, 789, 123, 98, 3, 22]
    for index, value in enumerate(t):
        print("i = {}, v = {}".format(index, value))

if __name__ == '__main__':
    main()
    exit(0)