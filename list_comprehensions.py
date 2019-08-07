"""
List Comprehensions
Readable, exspressive, and effective
"""
from math import factorial as fact

def is_prime(n):
    """
    Returns true for prime numbers false for prime numbers
    :param n:
    :return:
    """
    if n < 2:
        return False
    else:
        for x in range(2,n):
            if(n % x == 0):
                return False
    return True


def main():
    """
    Test funcion
    :return:
    """
    words = "Today I am very happy to lear about list comprehensions".split()
    print(words)
    data = []
    for word in words:
        #some analysis
        data.append(word)
    print(data)

    #Task: Find the length of the first 20
    # Factorial numbers
    digits=[]
    for x in range(20):
        digits.append(len(str(fact(x))))
        print("digit: {} factorial: {} length: {}".format(x, fact(x), len(str(fact(x)))))
    # use a list comprehension instead
    info = [len(str(fact(x))) for x in range(20)]
    print(info)

    #Set Comprehensions: ()'
    info2 = {len(str(fact(x))) for x in range(20)}
    print(info2)


    #dictionary comprehenions
    nba_teams = {'jazz':'SLC', 'warriors':'OAOKLAND', 'lakers':'LA', 'clippers':'LA'}
    teams_nba = {city:mascot for mascot, city in nba_teams.items()}
    print(teams_nba)

    prime = [i for i in range(10000000) if is_prime(i)]
    #filter predicates
    print(prime)

if __name__ == '__main__':
    main()
    exit(0)