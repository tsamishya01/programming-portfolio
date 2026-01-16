import sys

if len(sys.argv) < 2:
    print("Usage: python nl.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, "r") as f:
        for i, line in enumerate(f, start=1):
            print(f"{i}\t{line}", end='')  
except FileNotFoundError:
    print("File not found:", filename)
