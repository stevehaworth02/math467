from sympy import isprime

def fermat_prime(n):
    return 2**2**n + 1

def main():
    try:
        n = int(input("Enter how many Fermat numbers to check (based on exponent n): "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    for p in range(n):  # +2 so it includes the nth exponent starting from 2
        m = fermat_prime(p)
        prime_status = isprime(m)
        print(f"Number: {m} Is Prime: {str(prime_status).upper()}")

if __name__ == "__main__":
    main()


