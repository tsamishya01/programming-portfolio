def encrypt_reverse(message: str) -> str:
    no_spaces = message.replace(" ", "")
    return no_spaces[::-1]

msg = "hello world"
encrypted = encrypt_reverse(msg)
print("Original:", msg)
print("Encrypted:", encrypted) 
