import sys

if len(sys.argv) < 3:
    print("Usage: python grep.py <pattern> <filename>")
    sys.exit(1)

pattern = sys.argv[1]
filename = sys.argv[2]

try:
    with open(filename, "r") as f:
        for line in f:
            if pattern in line:
                print(line, end='') 
except FileNotFoundError:
    print("File not found:", filename)
