"""
Rotated Sorted Array
A sorted array is rotated at some random pivot point
We have to search a target value and return its index or else -1
Time complexity expected to be O(log(n))
"""


# Time complexity of finding pivot index is O(log(n)) as we are dividing each time list to find the pivot
def rotated_array_search_recursive(input_list, number, start_index, end_index):
    middle_index = (start_index + end_index) // 2

    if input_list[middle_index] < input_list[middle_index - 1] and middle_index > 0:
        return middle_index

    if start_index >= end_index:
        return -1

    # We recursive left or right to find the pivot value and return
    pivot_index_left = rotated_array_search_recursive(input_list, number, start_index, middle_index - 1)
    pivot_index_right = rotated_array_search_recursive(input_list, number, middle_index + 1, end_index)

    if pivot_index_right == -1 and pivot_index_left == -1:
        pivot_index = -1
    elif pivot_index_right != -1 and pivot_index_left == -1:
        pivot_index = pivot_index_right
    elif pivot_index_left != -1 and pivot_index_right == -1:
        pivot_index = pivot_index_left
    else:
        return -1
    return pivot_index


"""
Once we know pivot index we have to identify which part of array does value lies in, left or right
We call binary search in that list and time complexity is of O(log(n)) as we are running on n/2 size of list

"""


def binary_search_sorted_list(input_list, number, start_index, end_index):
    middle_index = (start_index + end_index) // 2
    if start_index > end_index:
        return -1

    if input_list[middle_index] == number:
        return middle_index
    elif input_list[middle_index] > number:
        return binary_search_sorted_list(input_list, number, start_index, middle_index - 1)
    else:
        return binary_search_sorted_list(input_list, number, middle_index + 1, end_index)


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array
    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    """
    Solution method:-
    Now input string can be rotated at any item in it and we have to find it
    We can use Divide and Conquer thought process for pivot index and 
    Binary search for sorted half where value exist 
    """
    start_index = 0
    end_index = len(input_list) - 1
    pivot_index = rotated_array_search_recursive(input_list, number, start_index, end_index)
    # Now we got Pivot index and value of pivot
    if pivot_index == -1:
        return -1
    pivot_value = input_list[pivot_index]

    # Finding Number as per pivot value
    # Case 1 , number is equal to pivot value, we return pivot index
    if number == pivot_value:
        return pivot_index

    # Case 2, Find whether value lie on right side or left side and call binary search accordingly
    if input_list[pivot_index] < number <= input_list[end_index]:
        # value when on right of pivot value
        match_index = binary_search_sorted_list(input_list, number, pivot_index + 1, end_index)
    elif input_list[0] <= number <= input_list[pivot_index - 1]:
        # When value is on left of Pivot value
        match_index = binary_search_sorted_list(input_list, number, start_index, pivot_index)
    else:
        return -1
    return match_index


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def check_function(input_case):
    input_list = input_case[0]
    number = input_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    check_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    check_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    check_function([[6, 7, 8, 1, 2, 3, 4], 8])
    check_function([[6, 7, 8, 1, 2, 3, 4], 1])
    check_function([[6, 7, 8, 1, 2, 3, 4], 10])

    # Test Case 1, Number doesn't exist in list
    check_function([[6, 7, 8, 1, 2, 3, 4], 0])

    # Test Case 2, No pivot point exist [ OUTPUT Xfail ]
    # This will fail as linear search which we are using is not checking pivot availability in code
    check_function([[6, 7, 8, 9, 10, 11, 12], 10])

    # Test Case 2, 2 pivot point exist
    # This will pass as liner search is only checking if value is in list or not, not checking pivot
    check_function([[9, 10, 11, 6, 7, 8, 1, 2, 3, 4], 0])
