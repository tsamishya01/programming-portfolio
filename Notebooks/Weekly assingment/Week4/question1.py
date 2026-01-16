def in_range_0_100(n: int) -> bool:
    return 0 <= n <= 100

for test in [-5, 0, 50, 100, 120]:
    print(test, "->", in_range_0_100(test))
