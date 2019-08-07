"""
Learn about scoping in python
"""
count = 0 #global object


def show_count():
    """
    Display the current count
    :return:
    """
    print(count)

def set_count(n):
    """
    Set the value of count
    :param n:
    :return:
    """
    global count
    count = n

def main():
    """

    :return:
    """
    show_count()
    set_count(9)
    show_count()


if __name__ == '__main__':
    main()
    exit(0)