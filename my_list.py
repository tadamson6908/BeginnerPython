"""
Learn about list()
"""


def main():
    """
    Test Function
    :return:
    """
    s = "show how to do it".split()
    print(s, type(s))
    print("Last member: ", s[-1])
    print("From 1 to one before the last member",s[:])
    #Make a copy of a list
    t = s[:] # deep copy
    print(t is s)

    # shallow copies
    # a list of list
    a =[[1,2], [3,4]]
    b = a[:]
    a[0][0] = 6
    print(a[0] is b[0])
    print("b = ",b)

    #repetition
    c = [21, 37]
    d = c * 4
    print(d)
    print(d[0] is d[1])
    s = [[-1,1]] * 5
    s[1].append(7)
    print(s)
    w = "the quick brown fox jumps over the lazy dog".split()
    print(w)
    i = w.index('fox')
    print("The index of fox is: ", i)

    #Membership testing with count()
    print("the value is ", w.count("the"))
    # Also test membership with in and not in
    print("37 in", 37 in [12, 22, 37, 99])
    #removing elements from list: index and del
    print(w)
    del w[3]
    print(w)
    w.remove("over")
    print(w)

    #rearranging list of elements
    g = [1, 11, 21, 1211, 113111]
    print("g =", g)
    g.reverse()
    print("reverse g", g)

    #sort method accepts two arguments, key, reverse
    d = [21, 33, 11, 77, 88, 33, 101, 1]
    print("d before", d)
    d.sort()
    print("d after", d)
    d = [21, 33, 11, 77, 88, 33, 101, 1]
    print("d before", d)
    d.sort(reverse=True)
    print("d after", d)

    w = "the quick brown fox jumps over the lazy dog".split()
    print(w)
    w.sort(key=len)
    print(w)

if __name__ == '__main__':
    main()
    exit(0)