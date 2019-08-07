"""
Learn about dictionaries
"""

def main():
    """
    Test function
    :return:
    """
    urls = {
        "google" : "www.google.com",
        "yahoo"  : "www.yahoo.com",
        "twitter": "www.twitter.com",
        "wsu"    : "weber.edu",
    }
    names_age = [('Alice', 32), ('Mario', 23), ('Hugo', 21)]
    d = dict(names_age)
    print(d)
    phonetic = dict(a='alpha', b='bravo', c='charlie', d='delta')
    print(phonetic)
    # make a copy
    e = phonetic.copy()
    print(e)
    stocks ={'GOOG':891, 'AAPL':416, 'IBM':194}
    print(stocks)
    stocks.update({'GOOG':999, 'YHOO':2})
    print(stocks)
    for key in stocks:
        print("{k} => {v}".format(k=key, v=stocks[key]))
    for val in stocks.values():
        print("val =", val)
    for key, val in stocks.items():
        print(key, val)
    print('GOOG' in stocks)


    isotopes = {
        'H' : [1,2,3],
        'He': [3,4],
        'Li': [6,7],
        'Be': [7,9,10],
        'B' : [10,11],
        'C' : [11,12,13,14]
    }
    print(isotopes)
    isotopes['H'] += [4,5,6,7]
    print.pprint(isotopes)
    isotopes['N'] = [13,14,15]
    print.pprint(isotopes)

if __name__ == '__main__':
    main()
    exit(0)