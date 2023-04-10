import unittest

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binary_search_recursive(s_list, s_elem):
    mid = len(s_list)//2
    if (s_list[mid] == s_elem):
        return mid
    elif (s_list[mid] < s_elem):
        return mid+1+binary_search_recursive(s_list[mid+1:], s_elem)
    elif (s_list[mid] > s_elem):
        return binary_search_recursive(s_list[:mid], s_elem)


def binary_search(s_list, s_elem):
    start = 0
    end = len(s_list)-1
    while (start <= end):
        mid = (start+end)//2
        if(s_list[mid]==s_elem):
            return mid
        elif(s_list[mid]<s_elem):
            start=mid+1
        elif(s_list[mid]>s_elem):
            end = mid-1
    return -1

class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        for x in range(0,10):
            self.assertEqual(binary_search(list1,x),x-1)


if __name__ == '__main__':
    unittest.main()