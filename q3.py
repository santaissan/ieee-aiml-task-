def is_prime(n):
    if n < 2:
        return False
    is_it_prime = False
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        is_it_prime = True
    return is_it_prime
print(is_prime(7))
print(is_prime(12))
n = int(input("Enter N: "))
primes = []
for num in range(2, n + 1):
    if is_prime(num):
        primes.append(num)
print(*primes)