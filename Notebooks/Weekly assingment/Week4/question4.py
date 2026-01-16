def remove_last_char(s: str) -> str:
    if len(s) <= 1:
        return s
    return s[:-1]

for test in ["hello", "a", ""]:
    print(repr(test), "->", repr(remove_last_char(test)))
