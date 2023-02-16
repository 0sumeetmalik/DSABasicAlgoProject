"""
Rearrange array elements so as to form two numbers such that their sum is maximum
assume: array in range [0,9]
constrain: number of digit cannot differ more than 1. means if there are 5 numbers, one can be 3 other 2, it cannot be 4 or 1
Time complexity = O(nlog(n))
"""
import pysnooper


# As inbuilt sort are restricted, created merge sort for the list which has time complexity of nlog(n)

def mergesort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    left = mergesort(left)
    right = mergesort(right)

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


# @pysnooper.snoop()
def rearrange_digits(input_list):
    # Sort using merge sort, not a inbuilt sort function. It has O(n log(n) time complexity
    sorted_list = mergesort(input_list)

    # extracting alternate largest elements to build
    x1 = sorted_list[::2]  # Time Complexity O(1)
    x2 = sorted_list[1::2]  # Time complexity O(1)

    # Joining elements to form a digit
    number_1 = int("".join(map(str, x1)))
    number_2 = int("".join(map(str, x2)))

    return [number_1, number_2]


def check_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    check_function([[1, 2, 3, 4, 5], [542, 31]])
    check_function([[4, 6, 2, 5, 9, 8], [964, 852]])

    # Test Case1 : large number of values
    check_function([[3, 4, 6, 7, 8, 9, 2, 1, 4, 9], [98642, 97431]])

    # Test case 2: Single digit in all elements
    check_function([[9, 9, 9, 9, 9, 9, 9, 9], [9999, 9999]])

    # Test Case 3: Most digit are zeros
    check_function([[7, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0], [700000, 60000]])
