password1 = input("Enter a new password: ")
password2 = input("Re-enter your password: ")

if password1 == password2:
    print("Password Set")
else:
    print("Error: passwords do not match.")
