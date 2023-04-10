def rec_fact(num):
    if(num==0):
        return 1
    return num*rec_fact(num-1)

def iter_fact(num):
    fact=1
    for x in range(1,num+1):
        fact*=x
    return fact

if(__name__ =='__main__'):
    inp_num = int(input("enter the number to get the factorial for: "))
    print(rec_fact(inp_num))
    print(iter_fact(inp_num))