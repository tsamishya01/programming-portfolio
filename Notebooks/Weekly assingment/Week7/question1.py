def unique_letters(s: str) -> list[str]:
    return sorted(set(s))

word = "cheese"
print(f"Unique letters in '{word}':", unique_letters(word))

