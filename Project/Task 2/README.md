
This program is a simple secure password verification system that adds an extra layer of authentication beyond just typing a password. Here's how it works:

The user is prompted to enter a password. The program immediately checks that the password is at least 9 characters long; if not, it exits.

If the password length is acceptable, it proceeds to security verification.

The program performs three random checks. In each check:

It picks a random position in the password.

It asks the user to enter the character at that position.

If the input matches the correct character at that position, the check passes. Otherwise, the program prints a failure message and exits immediately.

If all three random checks pass, the program prints a success message: "Security check passed. Access granted."

Essentially, it’s like a mini multi-factor verification, where the system tests if the user really knows their password without having to type it entirely. This is often used in banking or secure systems.
