import random

print("Welcome to the Secure Password Verification System")
print("--------------------------------------------------")

password = input("Enter your password: ")
password_length = len(password)

if password_length < 9:
    print("Password too short.")
    print("A valid password must be at least 9 characters long.")
    exit()

print("Password length accepted.")
print("Beginning security verification...\n")

checks_completed = 0
total_checks_required = 3

while checks_completed < total_checks_required:
    random_position = random.randint(1, password_length)

    user_input = input(
        f"Enter letter at position {random_position}: "
    )

    correct_character = password[random_position - 1]

    
    if user_input == correct_character:
        print("Correct")
        checks_completed += 1
    else:
        print("\nSecurity check failed.")
        print("Incorrect character entered.")
        exit()

print("\nSecurity check passed.")
print("Access granted.")
