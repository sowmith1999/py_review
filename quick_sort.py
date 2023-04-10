# Given an array of elements, sorts them using quick sort algorithm
import random
def quick_sort(s_list):
    # pick the last element in the array as the pivot
    if (len(s_list) <= 1):
        return s_list
    pivot = random.choice(s_list)
    lhs = []
    rhs = []
    mid = []
    for x in s_list:
        if (x > pivot):
            rhs.append(x)
        elif (x < pivot):
            lhs.append(x)
        else:
            mid.append(x)

    return quick_sort(lhs)+mid+quick_sort(rhs)


list1 = [6, 5, 7, 3, 8]

(print(quick_sort(list1)))

# use three way parition
# pick a random pivot
