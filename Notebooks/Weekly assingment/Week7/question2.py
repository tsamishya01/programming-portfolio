def letters_union(word1: str, word2: str) -> list[str]:
    return sorted(set(word1) | set(word2))  

def letters_intersection(word1: str, word2: str) -> list[str]:
    return sorted(set(word1) & set(word2)) 
def letters_symmetric_diff(word1: str, word2: str) -> list[str]:
    return sorted(set(word1) ^ set(word2)) 
w1 = "apple"
w2 = "Mango"

print("Union:", letters_union(w1, w2))          
print("Intersection:", letters_intersection(w1, w2))  
print("Symmetric difference:", letters_symmetric_diff(w1, w2)) 
