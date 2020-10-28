import numpy as np
import json
from time import time
import sys
import os

PRIMES_LIST = [2,3]
dirname = os.path.dirname(__file__)
PRIMES_PATH = os.path.join(dirname, 'primes.txt')

def get_primes(max_bound):
    global PRIMES_LIST
    for n in np.arange(PRIMES_LIST[-1], max_bound, 2):
        if is_prime(n):
            PRIMES_LIST.append(int(n))

        if n%10000 == 1:
            print(n)

    return PRIMES_LIST


def is_prime(n):
    ## n is smaller/equal than max bound of prime list, check if it's in list of primes. If it's not, it's not a prime number
    if n <= PRIMES_LIST[-1]:
        return n in PRIMES_LIST

    ## Check first if n is divisible by one prime number
    for p in PRIMES_LIST:
        if n%p == 0:
            return False

    ## Otherwise lookup numbers from last prime number checked -> sqrt(n)
    for div in np.arange(PRIMES_LIST[-1]+1, int(np.sqrt(n))+1, 2):
        if n%div == 0:
            return False

    ## If no divisor has been found, n is prime
    return True

def save_primes(primes, path=PRIMES_PATH):
    jsonfile = json.dumps(primes)
    f = open(path,"w")
    f.write(jsonfile)
    f.close()

def generated_primes(path=PRIMES_PATH):
    with open(path, 'r') as text_file:
        lines = text_file.read().split(',')
        primes = list(map(lambda p: int(p), lines))
        return primes

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(is_prime(n))
