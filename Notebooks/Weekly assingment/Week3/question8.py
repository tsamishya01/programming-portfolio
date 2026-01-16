table = int(input("Enter a number between -12 and 12: "))

if -12 <= table <= 12:
    if table < 0:
        table = abs(table)   
        for i in range(12, -1, -1):  
            print(f"{i} x {table} = {i * table}")
    else:
        for i in range(13): 
            print(f"{i} x {table} = {i * table}")
else:
    print("Error: number must be between -12 and 12.")
