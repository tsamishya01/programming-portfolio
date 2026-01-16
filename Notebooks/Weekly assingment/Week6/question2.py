def factors(n: int) -> list[int]:
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

print("Factors of 12:", factors(12)) 
print("Factors of 17:", factors(17))  
