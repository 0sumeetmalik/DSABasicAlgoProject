"""
Rotated Sorted Array
A sorted array is rotated at some random pivot point
We have to search a target value and return its index or else -1
Time complexity expected to be O(log(n))
"""


# Time complexity of finding pivot index is O(log(n)) as we are dividing each time list to find the pivot
def rotated_array_search_recursive(input_list, number, start_index, end_index):
    middle_index = (start_index + end_index) // 2

    if input_list[middle_index] < input_list[middle_index - 1]:
        return middle_index

    if start_index >= end_index:
        return -1

    # We recursive left or right to find the pivot value and return
    pivot_index_left = rotated_array_search_recursive(input_list, number, start_index, middle_index - 1)
    pivot_index_right = rotated_array_search_recursive(input_list, number, middle_index + 1, end_index)

    if pivot_index_right == -1 and pivot_index_left == -1:
        pivot_index = -1
    elif pivot_index_right != -1:
        pivot_index = pivot_index_right
    elif pivot_index_left != -1:
        pivot_index = pivot_index_left

    return pivot_index




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
    Solution method
    Now input string can be rotated at any item in it and we have to find it
    We can use Divide and Conquer thought process. We can find a middle point of string and see if it target is 
    """
    start_index = 0
    end_index = len(input_list) - 1
    pivot_index = rotated_array_search_recursive(input_list, number, start_index, end_index)
    # Now we got Pivot index and value of pivot
    pivot_value = input_list[pivot_index]

    # Finding Number as per pivot value
    # Case 1 , number is equal to pivot value, we return pivot index
    if number == pivot_value:
        return pivot_index

    # Case 2, number is greater than pivot value
    if input_list[pivot_index] < number <= input_list[end_index]:
        # value when on right of pivot value
        match_index = binary_search_sorted_list(input_list, number, pivot_index + 1, end_index)
    elif input_list[0] <= number <= input_list[pivot_index-1]:
        # When value is on left of Pivot value
        match_index = binary_search_sorted_list(input_list, number, start_index, pivot_index)

    return match_index


if __name__ == '__main__':
    arr = [6, 7, 8, 1, 2, 3, 4]
    number = 1
    print(rotated_array_search(arr, number))
