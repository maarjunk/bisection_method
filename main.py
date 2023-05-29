from src.mathematic_functions import *
from src.bisection_function import bisection

if __name__ == "__main__":
    print(f"the root of x-cos(x) is {bisection(-1,0,tabe1,0.001)}")
    print(f"the root of the e^x - 3x^2 is {bisection(0,1,tabe2,0.915)}")
