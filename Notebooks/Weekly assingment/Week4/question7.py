import statistics

temps_c = []

for i in range(6):
    value = input(f"Enter temperature {i+1} (e.g., 20C): ").strip()
    if value.endswith("C"):
        temps_c.append(float(value[:-1]))
    else:
        print("Invalid format, try again.")
        exit()

print("Maximum:", max(temps_c), "C")
print("Minimum:", min(temps_c), "C")
print("Mean:", statistics.mean(temps_c), "C")
