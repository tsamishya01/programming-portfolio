def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for num in [1, 2, 3, 4, 17, 20]:
    print(f"{num} is prime? {is_prime(num)}")
