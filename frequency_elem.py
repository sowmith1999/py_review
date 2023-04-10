#  Given an array of integers, find the frequency of each integer

def find_freq(s_list):
    freq_dict = dict()
    for x in s_list:
        if (freq_dict.get(x, 0)):
            freq_dict[x] += 1
        else:
            freq_dict[x] = 1
    return freq_dict


list1 = [1, 1, 1, 4, 5, 6, 8, 8]

print(find_freq(list1))