"""
Get a file from the web
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

Task 1: count the number of words in document
"""
from urllib.request import urlopen
from functions import even_or_odd as eo



def countWords(file):
    """

    :return:
    """
    #file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"
    with urlopen(file) as story:
        count = 0
        numWords = {}
        for line in story:
            line = line.decode("utf-8")
            #print(line)
            words = line.split()
            for word in words:
                if word in numWords:
                    numWords[word] += 1
                else:
                    numWords[word] = 1
        for item in numWords:
            print(item, "=>", numWords[item])

if __name__ == "__main__":
    countWords()
    exit(0)


        #count += len(words)
        #print(line)
