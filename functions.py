"""
Learn about functions/definitions
Use the keyword: def<name>()
"""


def even_or_odd(number):
    """
    determine if number if even or odd
    :print:  'even' on even numbers
              'odd' on odd numbers
    """
    if number % 2 == 0:
        print("even")
    else:
        print("odd")

def main():
    """

    :return:
    """
    #call function
    print(__name__)
    even_or_odd(89)
    even_or_odd(22)

if __name__ == "__main__":
    main()
    exit(0)