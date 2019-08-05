"""
Get a file from the web
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

Task 1: count the number of words in document
"""
from urllib.request import urlopen
file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"

with urlopen(file) as story:
    count = 0
    for line in story:
        words = line.split()
        count += len(words)
        #print(line)
    print(count)