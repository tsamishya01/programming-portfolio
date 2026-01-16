name = input("Please enter your name: ")

if name == "":
    print("Hello, Stranger!")
else:
    formatted_name = name.capitalize()
    print(f"Hello, {formatted_name}!")
