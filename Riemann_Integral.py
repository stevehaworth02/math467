from math import log
from scipy.integrate import quad
def li(x):
    # You write this using scipy.integrate or your own implementation
    result, error = quad(lambda t: 1 / log(t), 2, x)
    return result
x = 2000
approx_prime_count = li(x)
print(f"Approximate number of primes ≤ {x}: {approx_prime_count}")
