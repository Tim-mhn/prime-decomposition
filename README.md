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


- Algorithm Version 1

Combination of [Pollard Rho](https://en.wikipedia.org/wiki/Pollard's_rho_algorithm) algorithm, look-up in a list of pre-generated prime numbers and brute force search.

