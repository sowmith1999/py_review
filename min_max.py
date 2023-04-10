# Given an array of integer find the minimum and the maximum element

# Assumes that there are more than zero elements in the given list
def min_max(s_list):
    min_elem = max_elem = s_list[0]
    for x in s_list:
        if (x<min_elem):
            min_elem=x
        if(x> max_elem):
            max_elem=x
    return min_elem, max_elem

list1 = [-1, 2, 3, 4, 5, 6, 0]

print(min_max(list1))