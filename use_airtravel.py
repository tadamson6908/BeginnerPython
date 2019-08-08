"""
use flight class
"""
from airtravel import Flight, Aircraft

def main():
    """

    :return:
    """
    a1 = Aircraft("blah", "airbus", 22, 6)
    f = Flight("SN066",a1)
    f2 = Flight('SN013',a1)

    print(f, type(f))
    print(f.number())
    print(f2.number())
    f.alllocate_seat("1C", "John")
    f.alllocate_seat("11C", "Cindy")
if __name__ == '__main__':
    main()
    exit(0)