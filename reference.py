"""
Learn about references

"""

def modify(k):
    """

    :param k:
    :return:
    """
    #lists are passed by reference
    k.append(39)
    print("k = ", k)


def replace(g):
    """
    Replace input list
    :param g:
    :return:
    """
    g = [17, 48, 89, 36]
    print("g =", g)

def replace_content(g):
    """
    Replace the content of the list
    :param g: input list
    :return: nothing
    """
    g[0] = 88
    g[1] = 22
    g[2] = 44
    print("g = ", g)

def main():
    """

    :return:
    """
    m = [9,15,24]
    modify(m)
    print("m = ",m)
    replace(m)
    print("m = ", m)
    replace_content(m)
    print("m = ", m)


if __name__ == '__main__':
    main()
    exit(0)