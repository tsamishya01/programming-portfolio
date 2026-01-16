sweets = int(input("How many sweets are there? "))
pupils = int(input("How many pupils are present? "))

each = sweets // pupils
left_over = sweets % pupils

print(f"Each pupil gets {each} sweets.")
print(f"There will be {left_over} sweets left over.")
