def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min = ints[0]
    max = ints[0]
    for i in ints:
        if i > max:
            max = i
        if i < min:
            min = i
    return (min, max)

#Test Case 1
import random
test_list_1 = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(test_list_1)
#print ("Pass" if ((0, 9) == get_min_max(test_list_1)) else "Fail")
#expected: Pass

#Test Case 2
test_list_2 = [444444444444, 222222222]
#print(get_min_max(test_list_2))
#expected (222222222, 444444444444)

#Test Case 3
test_list_3 = [i for i in range(1,1000001)]
#print(get_min_max(test_list_3))
#expected (1, 1000000)

#Test Case 4
test_list_4 = [99]
#print(get_min_max(test_list_4))
#expected (99,99)