import sys
import statistics

temps_c = []

for arg in sys.argv[1:]:
    if arg.endswith("C"):
        try:
            temps_c.append(float(arg[:-1]))
        except ValueError:
            print(f"Invalid temperature ignored: {arg}")
    else:
        print(f"Invalid format ignored (must end in C): {arg}")

if not temps_c:
    print("No valid temperature arguments provided.")
else:
    print("Maximum:", max(temps_c), "C")
    print("Minimum:", min(temps_c), "C")
    print("Mean:", statistics.mean(temps_c), "C")
