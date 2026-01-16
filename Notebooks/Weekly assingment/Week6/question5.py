import random
import string

def encrypt_with_random_spacing(message: str) -> tuple[str, int]:
    interval = random.randint(2, 20)
    encrypted = ""
    for char in message:
        encrypted += char
       
        for _ in range(interval - 1):
            encrypted += random.choice(string.ascii_lowercase)
    return encrypted, interval


msg = "send cheese"
encrypted_msg, interval_used = encrypt_with_random_spacing(msg)
print("Original message:", msg)
print("Encrypted message:", encrypted_msg)
print("Interval used:", interval_used)
