"""
Find Floor value of Square root of the Integer without using any python library.
Example: 16 square root is 4, 27 square root is 5 as sqrt(27) = 5.196
Time complexity expected O(log(n))

"""
import math
import decimal
import copy


def sqrt(number):
    """
    :param number: Input variable whose square root we hve to find
    :return: Floor square root number
    """
    if number > 1:
        start_number = 1
    else:
        start_number = 0
    last_number = number
    return sqrt_recursive(number, start_number, last_number)


def sqrt_recursive(number, start_number, last_number):
    sq_root = round((start_number + last_number) / 2, 2)
    if sq_root * sq_root > number:
        last_number = sq_root
        return sqrt_recursive(number, start_number, last_number)
    elif math.isclose(sq_root * sq_root, number, abs_tol=0.1) or math.isclose(start_number, last_number, abs_tol=0.05):
        # sq_root = round(sq_root, 0)
        return math.floor(sq_root)
    elif sq_root < 1:
        return number
    else:
        start_number = sq_root
        return sqrt_recursive(number, start_number, last_number)


if __name__ == '__main__':
    print(sqrt(120))
    print("Pass" if (3 == sqrt(9)) else "Fail")
    print("Pass" if (0 == sqrt(0)) else "Fail")
    print("Pass" if (4 == sqrt(16)) else "Fail")
    print("Pass" if (1 == sqrt(1)) else "Fail")
    print("Pass" if (5 == sqrt(27)) else "Fail")
    print(sqrt(35))
