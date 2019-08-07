"""
Learn about collections: tuples, strings, Range, List, Dictionaries, Sets
"""

def do_tuples():
    """
    Practice tuples
    :return: nothing
    """
    #immutable sequence of arbitrary objects
    #Use () to define a tuple
    t = ("Ogden", 1.99, 2)
    print(t, type(t))
    print("Size ", len(t))
    print("One member:", t[0])
    for item in t:
        print(item)

    #a single value needs to end in comma for tuple
    t1 = (6, )
    print(t1, type(t1))
    #parenthesis are optional
    t2 = 1,2,3,4
    t_from_l = tuple([3,77,11])
    print(t_from_l)
    print(5 in(3, 6, 7, 8, 5))
    print(5 not in(3, 6, 7, 8, 5))

def min_max(items):
    """
    Return the minimum and maximum elements of a list
    :param items: collection
    :return: the minimum and maximum
    """

    return min(items), min(items)

def swap(in1, in2):
    """
    Swaps two values
    :param in1:
    :param in2:
    :return:
    """
    return in2, in1


def main():
    """

    :return:
    """
    do_tuples()
    # min, max = min_max([56, 79, 11, 12, 90])
    # print("min = ", min)
    # print("max =", max)

if __name__ == '__main__':
    main()
    exit(0)