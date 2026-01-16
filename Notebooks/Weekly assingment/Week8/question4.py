import sys

if len(sys.argv) < 2:
    print("Usage: python wc.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, "r") as f:
        lines = f.readlines()
        num_lines = len(lines)
        num_chars = sum(len(line) for line in lines)

    print(f"Lines: {num_lines}")
    print(f"Characters: {num_chars}")

except FileNotFoundError:
    print("File not found:", filename)
