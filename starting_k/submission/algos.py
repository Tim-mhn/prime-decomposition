import sys
from time import time
from pollard_rho import pollard
from generate_primes import generated_primes
from brute_force import brute_force
from prime_test import is_prime, pws_is_prime

print("generate primes called")
PRIMES_LIST = generated_primes()

def factorize_v1(n, ini_facto=False):

    ## Version 1 of factorization algorithm
    ## 1. Set a threshold of number of digits: TH
    ## 2. Use a pre-generated list of primes. Try to divide number by these primes numbers
    ## 3. If still composite and many digits, use pollard rho
    ## 4. If still composite, finish with brute force

    prime_factors_list = list()

    if ini_facto:
        prime_factors_list, n = initial_facto(n)

    POLLARD_TH = 1e6

    if digits(n) > POLLARD_TH:
        # Pollard_rho algo
        pollard_res = pollard(n)
        # If returns false, n is prime
        if not pollard_res:
            return prime_factors_list + [n]

        [p, q] = pollard_res
        return prime_factors_list + factorize_v1(p) + factorize_v1(q)

    else:
        return prime_factors_list + brute_force(n)

def factorize_v2(n, ini_facto=True):

    ## Version 1 of factorization algorithm
    ## 1. Set a threshold of number of digits: TH
    ## 2. Use a pre-generated list of primes. Try to divide number by these primes numbers
    ## 3. If still composite and many digits, use pollard rho
    ## 4. If still composite, finish with brute force

    prime_factors_list = list()
    start = time()
    print(f"Starting for {n}")
    if ini_facto:
        prime_factors_list, n = initial_facto(n)

    if n == 1:
        return prime_factors_list

    print(f"{time() - start} for initial facto. {n}")
    startp = time()
    isprime = pws_is_prime(n)
    print(f"is prime took {time() - startp}")
    if isprime:
        print(f"{n} was prime")
        print(prime_factors_list + [n])
        return prime_factors_list + [n]

    start = time()
    primes = prime_factors_list + brute_force(n)
    print(f"Brute force took {time()-start}s")
    print(f"{primes}\n\n")
    return primes


def initial_facto(n):
    prime_factors_list = list()
    for p in PRIMES_LIST:
        while n%p == 0:
            prime_factors_list.append(int(p))
            n = n/p

    return prime_factors_list, int(n)

def digits(n):
    return len(str(int(n)))

if __name__ == "__main__":
    start = time()
    n = int(sys.argv[1])
    print(factorize_v1(n, ini_facto=True))
    print(f"Took {time() - start}s")