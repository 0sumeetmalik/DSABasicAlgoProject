"""
Find Floor value of Square root of the Integer without using any python library.
Example: 16 square root is 4, 27 square root is 5 as sqrt(27) = 5.196
Time complexity expected O(log(n))

"""
"""
Idea : Divide the number to half of its value and check if half_value *2 is same as number if not further divide
It is similar to finding Pivot point in divide a conquer, here I have replace thinking of median to a Sq_root number
It has time complexity of Log(n)
"""

import math


def sqrt(number):
    """
    :param number: Input variable whose square root we hve to find
    :return: Floor square root number
    """
    if number > 1:
        start_number = 1
    elif number < 0 or number is None:
        return None
    else:
        start_number = 0
    last_number = number

    return sqrt_recursive(number, start_number, last_number)


def sqrt_recursive(number, start_number, last_number):
    """
    Using Divide and Conquer strategy.
    Dividing say 9 number to half > 4.5 and checking if 4.5* 4.5 is greater or smaller. If greater. Divide this further
    Next sq_root number will be 2.25 and then do check again. This way it will converge to SQRT which has tolerance
    Using isclose math function to get SQRT and then returning floor values
    """
    sq_root = round((start_number + last_number) / 2, 2)
    if sq_root * sq_root > number:
        last_number = sq_root
        return sqrt_recursive(number, start_number, last_number)
    elif math.isclose(sq_root * sq_root, number, abs_tol=0.1) or math.isclose(start_number, last_number, abs_tol=0.1):
        return math.floor(sq_root)
    elif sq_root < 1:
        return number
    else:
        start_number = sq_root
        return sqrt_recursive(number, start_number, last_number)


if __name__ == '__main__':
    print("Pass" if (3 == sqrt(9)) else "Fail")
    print("Pass" if (0 == sqrt(0)) else "Fail")
    print("Pass" if (4 == sqrt(16)) else "Fail")
    print("Pass" if (1 == sqrt(1)) else "Fail")
    print("Pass" if (5 == sqrt(27)) else "Fail")

    """
    3 Different test conditions
    """
    # Negative number input
    print("Pass" if (None == sqrt(-1)) else "Fail")

    # large Number
    print("Pass" if (3162 == sqrt(10000000)) else "Fail")

    # Any random value
    print("Pass" if (9 == sqrt(81)) else "Fail")
