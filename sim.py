"""
prime_plot.py  –  visualises π(x) vs two Riemann‑style approximations
Usage:  python prime_plot.py [N]
"""
import sys, math, matplotlib.pyplot as plt

# ---------- helpers ----------
def sieve_up_to(n):
    sieve = [True]*(n+1)
    sieve[0:2] = [False, False]
    for p in range(2, int(n**0.5)+1):
        if sieve[p]:
            sieve[p*p:n+1:p] = [False]*len(range(p*p, n+1, p))
    return [i for i, is_p in enumerate(sieve) if is_p]

def prime_count_curve(n, primes):
    pi = [0]*(n+1); count = 0; idx = 0
    for x in range(2, n+1):
        while idx < len(primes) and primes[idx] == x:
            count += 1; idx += 1
        pi[x] = count
    return pi

def li_curve(n):
    li, cur = [0.0]*(n+1), 0.0
    for x in range(2, n+1):
        cur += 1/math.log(x)
        li[x] = cur
    return li

def weighted_curve(n, primes):
    w = [0.0]*(n+1)
    for p in primes:
        k, power = 1, p
        while power <= n:
            for x in range(power, n+1):
                w[x] += 1/k
            k += 1; power *= p
    return w

# ---------- main ----------
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
primes      = sieve_up_to(N)
pi_vals     = prime_count_curve(N, primes)
li_vals     = li_curve(N)
weighted    = weighted_curve(N, primes)
xs          = list(range(N+1))

# plot 1
plt.figure(figsize=(8,5))
plt.plot(xs, pi_vals, label=r'$\pi(x)$ (actual)')
plt.plot(xs, li_vals, '--', label=r'$\mathrm{Li}(x)$')
plt.plot(xs, weighted, ':', label=r'weighted sum')
plt.xlabel('$x$'); plt.ylabel('Count')
plt.title('Prime counting and approximations')
plt.legend(); plt.tight_layout(); plt.show()

# plot 2
err_li = [pi_vals[i]-li_vals[i] for i in xs]
err_w  = [pi_vals[i]-weighted[i] for i in xs]
plt.figure(figsize=(8,4.5))
plt.plot(xs, err_li, label=r'$\pi(x)-\mathrm{Li}(x)$')
plt.plot(xs, err_w,  label=r'$\pi(x)-$weighted')
plt.axhline(0, linewidth=0.8)
plt.xlabel('$x$'); plt.ylabel('Error')
plt.title('Approximation errors')
plt.legend(); plt.tight_layout(); plt.show()
