def is_prime(pos_int):
    """Check if a positive integer is prime."""
    if pos_int <= 1:
        return False
    for i in range(2, int(pos_int**0.5) + 1):
        if pos_int % i == 0:
            return False
    return True

def main():
    try:
        upper_bound = int(input("Please enter the upper bound: "))
        if upper_bound <= 0:
            print("Please enter a positive integer.")
            return
        
        prime_list = []
        
        for number in range(1, upper_bound + 1):
            if is_prime(number):
                prime_list.append(number)
        
        # Calculate the number of primes and the percentage
        prime_count = len(prime_list)
        percentage = (prime_count / upper_bound) * 100 if upper_bound > 0 else 0
        
        # Print the prime numbers
        for prime in prime_list:
            print(prime)
        
        # Print the summary
        print(f"[{prime_count} primes found ({percentage:.2f}%)")

    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
