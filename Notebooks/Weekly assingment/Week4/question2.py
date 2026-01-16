def count_case(s: str):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

text = "Hello WORLD!"
u, l = count_case(text)
print(f"Uppercase: {u}, Lowercase: {l}")
