def largest_prime_factor(N):
    # Initialize the largest prime factor to 1
    largest_prime = 1
    
    # Remove all the factors of 2 from N
    while N % 2 == 0:
        largest_prime = 2
        N //= 2
    
    # Try dividing N by odd numbers starting from 3
    for i in range(3, int(N**0.5) + 1, 2):
        while N % i == 0:
            largest_prime = i
            N //= i
    
    # If N is still greater than 1, it is the largest prime factor
    if N > 1:
        largest_prime = N
    
    return largest_prime

# Input
N = int(input())
# Output
print(largest_prime_factor(N))
