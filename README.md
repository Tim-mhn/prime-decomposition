# prime-decomposition
Competition CS Advanced Algorithms #2 for prime number decomposition

Commands:
```bash
cd starting_k/submission
sh run.sh
```

This will run the prime factorization for each instance in public_dat/public_dataset.

Each instance contains 10 to 20 numbers.

Results will be stored in a generated dist folder

**Algorithms Versions**
*Algorthims can be find in starting_k/submissions/algos.py*

- Algorithm Version 1: Combination of [Pollard Rho](https://en.wikipedia.org/wiki/Pollard's_rho_algorithm) algorithm, look-up in a list of pre-generated prime numbers and smart trial division.

- Algorithm Version 2: Combination of look-up in a list of pre-generated prime numbers, primality test with [Baillie-PWS](https://en.wikipedia.org/wiki/Baillie%E2%80%93PSW_primality_test) and smart trial division

