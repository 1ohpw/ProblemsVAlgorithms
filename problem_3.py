def backwards_merge_sort(input_list):
    
    def merge(left, right):
        backwards_merged_list = []
        left_index = 0
        right_index = 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] > right[right_index]:
                backwards_merged_list.append(left[left_index])
                left_index += 1
            else:
                backwards_merged_list.append(right[right_index])
                right_index += 1
        
        backwards_merged_list += left[left_index:]
        backwards_merged_list += right[right_index:]
        
        return backwards_merged_list

    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2
    left = backwards_merge_sort(input_list[:mid])
    right = backwards_merge_sort(input_list[mid:])

    return merge(left, right)

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    backwards_sorted_list = backwards_merge_sort(input_list)
    n = 0
    m = 0
    for i, num in enumerate(backwards_sorted_list):
        if i % 2 == 0:
            n = n * 10 + num
        else:
            m = m * 10 + num
    return (n, m)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

#Test Case 1
test_case_1 = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case_1)
#expected: Pass

#Test Case 2
test_case_2 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case_2)
#expected: Pass

#Test Case 3
test_case_3 = [[1, 2], [1, 2]]
test_function(test_case_3)
#expected: Pass

#Test Case 4
test_case_4 = [[0], [0, 0]]
test_function(test_case_4)
#expected: Pass

#Test Case 5
test_case_5 = [[], [0, 0]]
test_function(test_case_5)
#expected: Pass

