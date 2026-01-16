import sys
import urllib.request

if len(sys.argv) < 2:
    print("Usage: python check_url.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        print("Website is reachable. HTTP status:", response.status)
except Exception as e:
    print("Website is NOT reachable.")
    print("Error:", e)
