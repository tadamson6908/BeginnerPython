"""
Generator objects are a a cross between comprehensions and generator functions
Syntax: Similar to list comprehension:
    (expr(item) for item in iterable)
"""
from list_comprehensions import is_prime

def main():
    """

    :return:
    """
    #list with one million square numbers
    m_sq = ( x for x in range(1,10001) if(is_prime(x)))
    print(m_sq, type(m_sq))
    print(sum(m_sq))


if __name__ == '__main__':
    main()
    exit(0)