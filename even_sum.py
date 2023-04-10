def even_sum(num_list):
    sum=0
    for x in num_list:
        if(x%2==0):
            sum+=x
    return sum

if(__name__=='__main__'):
    inp_list = [int(x) for x in input("Enter the list of number separated by comma: ").split(',')]
    print(even_sum(inp_list))