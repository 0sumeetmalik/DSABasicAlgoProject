"""
Min and Max of Unsorted Array
Find smallest and largest integer from an unsorted list in O(n)

Also< try to get it in Single Traversal
Note: don't use Max and Min functions
"""
import random
import pysnooper


# @pysnooper.snoop()
"""
Time complexity O(n) and single traversal to get min and max without using inbuilt functions
"""


def get_min_max(ints):
    # print(ints)
    min_value = 0
    max_value = 0

    for i in range(len(ints)):
        if ints[i] < min_value:
            min_value = ints[i]
        if ints[i] > max_value:
            max_value = ints[i]

    return (min_value, max_value)


if __name__ == '__main__':
    l = [i for i in range(0, 10)]
    random.shuffle(l)
    print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

    # Test case 1 : negative values
    x = [7, -1, 5, 6, 9, 8, 2, 1, 3, 4]
    print("Pass" if ((-1, 9) == get_min_max(x)) else "Fail")

    # Test case 2 : No Input
    x = []
    print("Pass" if ((0, 0) == get_min_max(x)) else "Fail")

    # Test case 3: Large number of values
    x = [48, 32, 56, 64, 88, 0, 96, 24, 8, 80, 16, 72, 40]
    print("Pass" if ((0, 96) == get_min_max(x)) else "Fail")
