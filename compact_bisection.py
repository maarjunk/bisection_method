"""
in this module we create some math function to
use them in the bisection function
"""
import math


def tabe1(x: float) -> float:
    return x + math.cos(x)


def tabe2(x: float) -> float:
    return math.exp(x) - (3 * (x ** 2))


"""
in this module we are going to implement
bisection method for calculate the root of a function
"""


def bisection(a: float, b: float, f: "function", c: float) -> float:
    """
    from here we use persian too
    :param a: sar baze
    :param b: tahe baze
    :param f: tabe mad nazar (baiiad dar biron in function busection tarif shavad)
    :param c: maeghdari ke mi khahim javab akhsr az on kamtar bashe
    :return: tool rishe ba meghdar kamtar az c
    """

    while True:
        x = (a + b) / 2
        if (f(a) * f(x)) < 0:
            b = x
        elif (f(a) * f(x)) > 0:
            a = x
        elif x < c:
            return x
        else:
            pass



if __name__ == "__main__":
    print(f"the root of x-cos(x) is {bisection(-1,0,tabe1,0.001)}")
    print(f"the root of the e^x - 3x^2 is {bisection(0,1,tabe2,0.915)}")

