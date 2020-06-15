def binary_search(input_list, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    if input_list[mid] == target:
        return mid
    elif input_list[mid] < target:
        return binary_search(input_list, target, mid + 1, right)
    else:
        return binary_search(input_list, target, left, mid - 1)

def find_pivot(input_list, left, right):
    mid = right + left // 2
    if mid == 0 or input_list[mid] < input_list[mid - 1]:
        return mid
    elif input_list[mid] > input_list[0]:
        return find_pivot(input_list, mid + 1, right)
    else:
        return find_pivot(input_list, left, mid - 1)


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    pivot = find_pivot(input_list, 0, len(input_list) - 1)
    left = 0
    right = len(input_list) - 1

    if number == right:
        return input_list[right]
    elif number > input_list[right]:
        right = pivot - 1
    else:
        left = pivot
    
    return binary_search(input_list, number, left, right)

#Test Case 1
test_list_1 = [6, 7, 8, 9, 10, 1, 2, 3, 4]
#print(rotated_array_search(test_list_1, 6))
#expected: 0

#Test Case 2
#print(rotated_array_search(test_list_1, 1))
#expected: 5

#Test Case 3
test_list_2 = [6, 7, 8, 1, 2, 3, 4]
#print(rotated_array_search(test_list_2, 8))
#expected: 2

#Test Case 4
#print(rotated_array_search(test_list_2, 1))
#expected: 3

#Test Case 5
#print(rotated_array_search(test_list_2, 10))
#expected: -1

#Test Case 6
test_list_3 = [999999999, 1, 2, 3, 4]
#print(rotated_array_search(test_list_3, 999999999))
#expected: 0

#Test Case 7
test_list_4 = [1]
#print(rotated_array_search(test_list_4, 1))
#expected: 0

#Test Case 7
test_list_5 = [4001, 4000]
#print(rotated_array_search(test_list_5, 4000))
#expected: 1

