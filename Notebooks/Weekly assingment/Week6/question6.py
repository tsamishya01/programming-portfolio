def decrypt_with_interval(encrypted_message: str, interval: int) -> str:
     return encrypted_message[0::interval]


decrypted_msg = decrypt_with_interval
print("Decrypted message:", decrypted_msg)
