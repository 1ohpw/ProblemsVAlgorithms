def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    def sort_012_helper(left, next_0, next_2):
        if left > next_2:
            return
        if input_list[left] == 0:
            input_list[left] = input_list[next_0]
            input_list[next_0] = 0
            return sort_012_helper(left + 1, next_0 + 1, next_2)
        elif input_list[left] == 1:
            return sort_012_helper(left + 1, next_0, next_2)
        elif input_list[left] == 2:
            input_list[left] = input_list[next_2]
            input_list[next_2] = 2
            return sort_012_helper(left, next_0, next_2 - 1)

    sort_012_helper(0, 0, len(input_list) - 1)
    return input_list
    

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

#Test Case 1
#test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
#expected: [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
#expected: Pass

#Test Case 2
#test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
#expected: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
#expected: Pass

#Test Case 3
#test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
#expected: [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
#expected: Pass

#Test Case 4
#test_function([2, 1, 0])
#expected: [0, 1, 2]
#expected: Pass

#Test Case 5
#test_function([1])
#expected: [1]
#expected: Pass

#Test Case 6
#test_function([])
#expected: []
#expected: Pass


