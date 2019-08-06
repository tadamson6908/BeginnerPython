"""
Rename files from a folder
address = http://icarus.cs.weber.edu/~hvalle/hafb/prank.zip
"""
from os import listdir, rename, chdir, getcwd
import re


def renameFiles(fileLoc):
    """
    Reads files in a folder and renames them appropriately
    :param fileLoc:
    :return:
    """
    files = listdir(fileLoc)
    currDir = getcwd()
    chdir(fileLoc)
    for f in files:
        s = re.sub("\d+", "", f)
        #src = fileLoc+ "\\" + f
        #dst = fileLoc + "\\" + s
        #print(src)
        rename(f,s)
    chdir(fileLoc)







def main():
    """
    tests program functions
    :return:
    """
    renameFiles(r"C:\Users\thomasadamson\Desktop\prank\prankOrig")



if __name__ == '__main__':
    main()
    exit(0)