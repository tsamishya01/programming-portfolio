import statistics

temps_c = []

while True:
    value = input("Enter temperature (e.g., 20C), or press Enter to finish: ").strip()

    if value == "":
        break

    if value.endswith("C"):
        temps_c.append(float(value[:-1]))
    else:
        print("Invalid format. Try again.")

if temps_c:
    print("Maximum:", max(temps_c), "C")
    print("Minimum:", min(temps_c), "C")
    print("Mean:", statistics.mean(temps_c), "C")
else:
    print("No temperatures entered.")
