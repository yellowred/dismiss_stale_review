#!/usr/bin/env python3
import random
import math

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check divisibility by numbers of the form 6k±1 up to sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

def generate_random_prime(min_val=2, max_val=1000):
    """Generate a random prime number within the given range."""
    print("Started to generate")
    while True:
        num = random.randint(min_val, max_val)
        if is_prime(num):
            return num

def main():
    print("hello forest people and mountain people!")
    prime = generate_random_prime()
    print(f"Here's a random prime number for you: {prime}")

if __name__ == "__main__":
    main()
