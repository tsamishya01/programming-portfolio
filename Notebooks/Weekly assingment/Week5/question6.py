import sys
import shutil
import os

if len(sys.argv) < 2:
    print("Usage: python backup_file.py <filename>")
    sys.exit(1)

original = sys.argv[1]

if not os.path.exists(original):
    print("Error: file does not exist.")
    sys.exit(1)

backup = original + ".bak"

shutil.copy(original, backup)

print(f"Backup created: {backup}")
