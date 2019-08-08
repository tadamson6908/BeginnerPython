"""
Learn about generator functions
- Describe iterables series with code functions
-Are lazy evaluated: the next value in the sequence is computed on demand
-Can model infinite series/sequences: data streams, mathematical series with no end
- Can use pipelines

use the yield keyword
"""


def gen123():
    yield 1
    yield 2
    yield 3

def gen246():
    print("about to yield 2")
    yield 2
    print("about to yield 4")
    yield 4
    print("about to yield 6")
    yield 6
    print("about to return")
def main():
    """

    :return:
    """
    g = gen123()
    print(g, type(g))
    print(next(g))
    print(next(g))
    #Iterate over the generator function
    for v in gen123():
        print(v)

if __name__ == '__main__':
    main()
    exit(0)