"""
Simulate 6000 rolls of a die
"""
import random



def roll():
    return random.randint(1,6)


def main():
    """
    test function
    :return:
    """
    track = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in range(6000):
        track[roll()] += 1;
    for num, freq in track.items():
        print("{} was rolled {} times".format(num, freq) )
        print("Mean = ", freq/6000)
if __name__ == '__main__':
    main()
    exit(0)