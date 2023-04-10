from math import sqrt as sqrt
from math import ceil as ceil


def is_prime(num):
    for x in range(2, ceil(sqrt(num))+1):
        if(num%x == 0):
            return False
    return True

if __name__ == '__main__':
    inp_num = int(input("Enter a number to check if it is a prime"))
    print(is_prime(inp_num))