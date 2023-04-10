def bubble_sort(s_list):
    list_len = len(s_list)
    for i in range(0,list_len):
        for j in range(0, list_len-i-1):
            if(s_list[j]>s_list[j+1]):
                s_list[j],s_list[j+1] = s_list[j+1], s_list[j]
    return s_list

if(__name__=='__main__'):
    list1 = [3, 1 , 6, 5, 0]
    arr = bubble_sort(list1[:])

    print(arr)
