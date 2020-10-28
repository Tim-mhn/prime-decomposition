import numpy as np
import sys

def brute_force(num):
    '''
    This function collectes all prime factors of given number and prints them.
    '''
    prime_factors_list = []
    while num % 2 == 0:
        prime_factors_list.append(2)
        num /= 2
    for i in range(3, int(np.sqrt(num))+1, 2):
        while num % i == 0:
            prime_factors_list.append(i)
            num /= i
    if num > 2:
        prime_factors_list.append(int(num))
    return prime_factors_list


if __name__ == "__main__":
    n = int(sys.argv[1])
    print(brute_force(n))