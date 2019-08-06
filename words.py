"""
Get a file from the web
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

Task 1: count the number of words in document
"""
from urllib.request import urlopen
from functions import even_or_odd as eo



def countWords(file):
    """
    Count words to url file
    :param file: url to file
    :return: words from file in an list
    """
    data = []
    with urlopen(file) as story:
        for line in story:
            line = line.decode("utf-8")
            words = line.split()
            for word in words:
                data.append(word)
    return data

def print_items(items):
    """
    Prints items in a list
    :param items: An input list
    :return:
    """
    for item in items:
        print(item)


def main():
    """
    Test functions in class
    :return:
    """
    words = countWords("http://icarus.cs.weber.edu/~hvalle/hafb/words.txt")
    print_items(words)




if __name__ == "__main__":
    main();
    exit(0)


        #count += len(words)
        #print(line)
