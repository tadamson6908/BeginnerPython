"""
Learn about python return semantics and how python functions
handle arguments.
"""
import time

def banner(message, border = '*'):
    """
    Prints the message with a border of input character border of border
    :param message: in message
    :param border:
    :return:
    """
    message = border + message + border
    border *= len(message)
    print(border)
    print(message)
    print(border)

def egg(var):
    """
    returns a variable back to the user
    :param var:
    :return:
    """
    return var

def add_spam(menu=None):
    """
    Add spma to the menu list
    :param menu:
    :return: menu list
    """
    if menu is None:
        menu =[]
    menu.append("spam")
    return menu



def sum_two(num1,num2=8):
    """
    Sum two input objects
    :param num1: object 1
    :param num2: object 2 (optionl), default to 8
    :return:
    """
    total = num1 + num2
    print(num1, "+", num2, "=", total)
    return total

def main():
    """

    :return:
    """
    c = [6,10,20]
    e = egg(c)
    print(c is e)
    n1 = 3
    n2 = 9
    sum_two(n1,n2)
    sum_two(n1)
    banner("pineapple")
    banner("Weber State", "+")
    breakfast = ["eggs", "bacon"]
    add_spam(breakfast)
    print("Breakfast = ", breakfast)

if __name__ == '__main__':
    main()
    exit(0)