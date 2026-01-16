BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password1 = input("Enter a new password: ")
    password2 = input("Re-enter your password: ")

    if password1 != password2:
        print("Error: passwords do not match. Try again.\n")
        continue

    if len(password1) < 8 or len(password1) > 12:
        print("Error: password must be between 8 and 12 characters long.\n")
        continue

    if password1 in BAD_PASSWORDS:
        print("Error: that password is too common. Choose another one.\n")
        continue

    print("Password Set")
    break
