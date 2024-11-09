
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

#
try:
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    
    if start > end:
        print("Invalid range. Start should be less than or equal to End.")
    else:
        
        prime_numbers = find_primes_in_range(start, end)
        if prime_numbers:
            print(f"Prime numbers between {start} and {end}: {prime_numbers}")
        else:
            print(f"There are no prime numbers between {start} and {end}.")
except ValueError:
    print("Invalid input. Please enter valid integers.")