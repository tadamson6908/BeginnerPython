"""
When working with iterators, generators, etc
Look at the documentation for the itertools module
"""
from itertools import islice, count, chain
from list_comprehensions import is_prime

def main():
    """

    :return:
    """
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print(thousand_primes, type(thousand_primes))
    print("List og first 1k prime numbers:", list(thousand_primes))
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print("List og first 1k prime numbers:", sum(thousand_primes))
    #other built_ins use with itertools: any, all
    print(any([False,False,False,True]))
    print(all([False,False,True]))
    print(any([is_prime(x) for x in range(1328,1362)]))
    names = ["London", "New York", "ogden"]
    print(all([s.istitle() for s in names]))
    #another built-in: zip()
    monday = [12,14,14,15,15,16,15,13,10,9]
    tuesday = [13,14,15,15,16,17,16,16,12,12]
    sunday = [2,2,5,7,9,10,9,6,4,4]

    # for temps in zip(monday, tuesday, sunday):
    #     print("min={:4.1f}, max={4.1f}, avg={4.1f}".format(
    #         min(temps), max(temps), sum(temps)/len(temps)
    #     ))
    all_temps = chain(sunday, monday, tuesday)
    print("All temperatures > 0", all(t>0 for t in all_temps))



if __name__ == '__main__':
    main()
    exit(0)