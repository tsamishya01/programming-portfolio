table = int(input("Enter a number between 0 and 12: "))

if 0 <= table <= 12:
    for i in range(13):
        print(f"{i} x {table} = {i * table}")
else:
    print("Error: number must be between 0 and 12.")
