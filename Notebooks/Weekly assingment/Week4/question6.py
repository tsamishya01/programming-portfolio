def c_to_f(c):
    return (c * 9/5) + 32

temp = input("Enter temperature (for example 20C): ").strip()

if temp[-1] == "C":
    number = float(temp[:-1])   
    fahrenheit = c_to_f(number)
    print(f"{fahrenheit}F")
else:
    print("Error: temperature must end with C.")
