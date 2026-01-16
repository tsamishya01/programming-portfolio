from collections import Counter

def top_six_letters(message: str):
    message = message.lower()  # case-insensitive
    letters_only = [c for c in message if c.isalpha()] 
    counts = Counter(letters_only)
    return counts.most_common(6)

msg = "This is an example message to demonstrate frequency counting."
top_six = top_six_letters(msg)
print("Six most common letters and counts:")
for letter, count in top_six:
    print(f"{letter}: {count}")
