students = int(input("How many students? "))
group_size = int(input("Required group size? "))

groups = students // group_size
left_over = students % group_size

if left_over == 1:
    print(f"There will be {groups} groups with 1 student left over.")
else:
    print(f"There will be {groups} groups with {left_over} students left over.")
