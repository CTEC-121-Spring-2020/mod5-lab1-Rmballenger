"""
CTEC 121
Robert Ballenger
Module 5 Lab 1
Learning functions
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""


def main1():
    print()
    print("happy birthday to you!")
    print("happy birthday to you!")
    print("Happy birthday, dear Fred...")
    print("Happy birthday to you!")


""" IPO happy()
Input(s): none
Process: Prints/outputs "happy birthday to you!"
Output: none
"""


def happy():
    print("Happy birthday to you!")


def main2():
    print()
    happy()
    happy()
    print("Happy birthday, dear Fred...")
    happy()
    print()


# generalize for any person
'''IPO happyBDay()
Input(s): a name
Process: prints/outputs verse line of happy birthday song
Output: prints to terminal screen
'''


def happyBday(name):
    print("Happy birthday, dear ", name, "...", sep="")


def main3():
    print()
    happy()
    happy()
    happyBday("Yoshi")
    happy()
    print()

# combine song into a function


def singHappyBDay(name):
    happy()
    happy()
    happyBday(name)
    happy()
    print()


def main4():
    singHappyBDay("Fred")
    singHappyBDay("Lucy")
    singHappyBDay("Bill")
    userName = input("What's your name?\n")
    singHappyBDay(userName)


main4()
