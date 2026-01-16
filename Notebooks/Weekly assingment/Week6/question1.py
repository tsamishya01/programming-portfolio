def to_binary(n: int) -> str:
    if n < 0:
        raise ValueError("Only positive integers allowed")
  
    return bin(n)[2:] 

print("Binary of 13:", to_binary(13)) 
print("Binary of 255:", to_binary(255))  
