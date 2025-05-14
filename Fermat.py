from sympy import isprime

def mersenne_number(p):
    return 2**p - 1

def main():
    try:
        n = int(input("Enter how many Mersenne numbers to check (based on exponent p): "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    for p in range(2, n + 2):  # +2 so it includes the nth exponent starting from 2
        m = mersenne_number(p)
        prime_status = isprime(m)
        print(f"Number: {m} Is Prime: {str(prime_status).upper()}")

if __name__ == "__main__":
    main()
