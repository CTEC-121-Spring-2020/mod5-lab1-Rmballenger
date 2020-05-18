# Doesnt return anything


def someFunction1():
    return


def someFunction2():
    return 123


def someFunction3():
    return 456, 789


def main():
    print()
    print(someFunction1())
    print()
    print(someFunction2())
    x = someFunction2()
    print(x)
    x, y = someFunction3()
    print(x, y)
    print()


main()
