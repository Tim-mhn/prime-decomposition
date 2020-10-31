import numpy as np
import sys

def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i: int = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def pws_is_prime(n: int) -> bool:
    # Inspired by https://en.wikipedia.org/wiki/Baillie%E2%80%93PSW_primality_test
    # Performs 2 tests:
    # 1. Miller Rabin strong probable prime test
    # 2. If successful, strong Lucas probable prime
    # If successful, n is very very likely to be prime
    miller_probable_prime = deterministic_miller_rabin(n)
    if not miller_probable_prime:
        return False

    return isLucasPseudoprime(n)


def deterministic_miller_rabin(n):

    # Deterministic miller rabin pseudo primarlity test
    # Inspired by https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    # If False: n is definitely not prime
    # If True: n is pseudo-prime aka very likely to be prime

    # If number is even, it's a composite number
    if n%2 == 0:
        return False

    # Write n as n-1 = d * 2**r
    r = 0
    even = n-1
    while (even%2 == 0):
        r += 1
        even = even//2

    d = even%2

    # WitnessLoop: for all a in the range [2, min(n−2, ⌊2(ln n)2⌋)]:
    for a in np.arange(2, min(n-2, int(2* (np.log(n))**2 ))):
        x = a**d % n
        if (x == 1) or (x == n-1):
            continue # Back for for loop

        back2outer_loop = False
        for _ in np.arange(r-1):
            x = x**2 % n
            if x == n-1:
                # Break current for loop and go back to 'a' loop
                back2outer_loop = True
                break
        # Go back to outer 'for a in' loop
        if back2outer_loop:
            continue

        return False # Not prime
    return True # Pseudoprime : very likely to be prime !



def gcd(a,b): # euclid's algorithm
    if b == 0: return a
    return gcd(b, a%b)

def jacobi(a, m):
    # assumes a an integer and
    # m an odd positive integer
    a, t = a % m, 1
    while a != 0:
        z = -1 if m % 8 in [3,5] else 1
        while a % 2 == 0:
            a, t = a / 2, t * z
        if a%4 == 3 and m%4 == 3: t = -t
        a, m = m % a, a
    return t if m == 1 else 0

def selfridge(n):
    d, s = 5, 1
    while True:
        ds = d * s
        if gcd(ds, n) > 1:
            return ds, 0, 0
        if jacobi(ds, n) == -1:
            return ds, 1, (1 - ds) / 4
        d, s = d + 2, s * -1

def lucasPQ(p, q, m, n):
    # nth element of lucas sequence with
    # parameters p and q (mod m); ignore
    # modulus operation when m is zero
    def mod(x):
        if m == 0: return x
        return x % m
    def half(x):
        if x % 2 == 1: x = x + m
        return mod(x / 2)
    un, vn, qn = 1, p, q
    u = 0 if n % 2 == 0 else 1
    v = 2 if n % 2 == 0 else p
    k = 1 if n % 2 == 0 else q
    n, d = n // 2, p * p - 4 * q
    while n > 0:
        u2 = mod(un * vn)
        v2 = mod(vn * vn - 2 * qn)
        q2 = mod(qn * qn)
        n2 = n // 2
        if n % 2 == 1:
            uu = half(u * v2 + u2 * v)
            vv = half(v * v2 + d * u * u2)
            u, v, k = uu, vv, k * q2
        un, vn, qn, n = u2, v2, q2, n2
    return u, v, k

def isLucasPseudoprime(n):
    n = int(n)
    if n == 1:
        return True
    print(f"Lucas Pseudoprime for {n}")
    d, p, q = selfridge(n)
    if p == 0: return n == d
    u, v, k = lucasPQ(p, q, n, n+1)
    return u == 0