"""
Given an input array of 0,1,2 sort the array in single traversal, Not allowed to use any sorting functions
"""
import pysnooper


# @pysnooper.snoop()
def sort_012(input_list):
    """
    Idea is to create 3 list which contains specifically 0,1,2 and then just join them when you return
    We will be able to execute this in single traversal

    :param input_list:
    :return: sorted list of 012
    """
    list_0 = list()
    list_1 = list()
    list_2 = list()

    for item in input_list:
        if item == 0:
            list_0.append(0)
        elif item == 1:
            list_1.append(1)
        elif item == 2:
            list_2.append(2)
        else:
            return -1

    return list_0 + list_1 + list_2


def check_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    check_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    check_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    check_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

    # Test case 1, when one digit is missing
    check_function([0, 2])

    # Test case 2, when digit beyond 0,1,2 exist in it, this will not be catched by check function,
    # XFail, as it will return -1
    check_function([0, 1, 2, 4])

    # Test case 3, Single digit in list
    check_function([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
