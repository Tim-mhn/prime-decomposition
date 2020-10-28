import numpy as np
import sys

def pollard(n):
    ## Factorizes (n = p * q) input and performant to find non-trivial factor
    n = int(n)
    x = 2
    y = 2
    d = 1

    while d == 1:
        x = g(x, n)
        y = g(g(y, n), n)
        try:
            d = np.gcd(np.abs(x - y), n)
        except Exception:
            raise ValueError(f"Error in pollard with {x}, {y} or {n}")

    if d == n:
        return False
    else:
        return [d, int(n/d)]

def g(x, n):
    return int((x**2+1)%n)


if __name__ == "__main__":
    n = int(sys.argv[1])
    print(pollard(n))
