"""
learn about iterable, iterator objects
Use the built-in iterator iter() and next()
iter creates and iterable object,
next fetches the next element in the iterable object
"""


def first(iterable):
    """
    Return the next member of the list IF available
    :param iterable:
    :return: Next member or
    """
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")

def main():
    """

    :return:
    """
    iterable = ["Spring", "Summer", "Fall", "Winter"]
    iterator = iter(iterable)
    print(type(iterator), iterator)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

if __name__ == '__main__':
    main()
    exit(0)