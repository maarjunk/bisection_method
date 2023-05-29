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
