password1 = input("Enter a new password: ")
password2 = input("Re-enter your password: ")

if password1 != password2:
    print("Error: passwords do not match.")
elif len(password1) < 8 or len(password1) > 12:
    print("Error: password must be between 8 and 12 characters long.")
else:
    print("Password Set")
