"""
Learn about exceptions
"""
import sys

def convert(s):
    """
    Converts a string to an int
    :param s:
    :return:
    """
    try:
        return int(s)
    except Exception as e:
        print("Conversion error: {}".format(e), file=sys.stderr)
        return -1

def sqrt(x):
    """
    Compute the square root using the methods of Heron of Alexandria
    :param x: Number to compute square root
    :return: the square root of x
    """
    guess = x
    i = 0
    try:
        while guess*guess != x and i < 20:
            guess = (guess + x/guess)/2.0
            print("guess = ", guess)

            i += 1
    except ZeroDivisionError as e:
        raise ValueError()
    return guess





def main():
    """

    :return:
    """
    # print(convert("11"))
    # print(convert("Hello"))
    # print(convert([1,4,8]))
    print(sqrt(400000000))

if __name__ == '__main__':
    main()
    exit(0)