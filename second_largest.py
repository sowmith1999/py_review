#  given an array of integers, finds the second largest element

def second_largest(s_list):
    max_elem = max_jr = s_list[0]
    for x in s_list:
        if (x > max_elem):
            max_jr = max_elem
            max_elem = x
        elif (x < max_elem and x > max_jr):
            max_jr = x
    return max_jr

list1 = [1, 2, 3, 4, 5, 6, 7, 8]

print(second_largest(list1))