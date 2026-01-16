import sys
import string

DICTIONARY_FILE = "/usr/share/dict/words"

if len(sys.argv) < 2:
    print("Usage: python spell.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(DICTIONARY_FILE, "r") as f:
        dictionary = set(word.strip().lower() for word in f)
except FileNotFoundError:
    print("Dictionary file not found:", DICTIONARY_FILE)
    sys.exit(1)

try:
    with open(filename, "r") as f:
        for line in f:
            for word in line.split():
              
                word_clean = word.strip(string.punctuation).lower()
                if word_clean and word_clean not in dictionary:
                    print(word_clean)
except FileNotFoundError:
    print("File not found:", filename)
