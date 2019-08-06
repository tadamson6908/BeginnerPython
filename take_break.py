"""
Set an alarm to take a break by playing a youtube video
"""

import webbrowser
import time




def openWebPage(url):
    """
    Opens a webpage given a url
    :param url: Input location of webpage to open
    :return:
    """
    webbrowser.open(url)




def main():
    """
    Tests the programs functionality
    :return:
    """
    for i in range(2):
        #delay "sleep"
        time.sleep(60*60)#1 hour
        url = "https://www.youtube.com/watch?v=vMlGBFXiC00"
        openWebPage(url)
    pass





if __name__ == "__main__":

    main();
    exit(0)