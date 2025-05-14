from math import log, floor, isqrt

def is_prime(n):
    if n < 2: return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def pi_weighted(x):
    result = 0.0
    for p in range(2, x + 1):
        if is_prime(p):
            n = 1
            while True:
                power = p ** n
                if power > x:
                    break
                result += 1 / n
                n += 1
    return result

x = 2000
weighted_count = pi_weighted(x)
print(f"Weighted prime power count ≤ {x}: {weighted_count:.6f}")
