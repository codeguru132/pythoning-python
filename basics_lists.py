﻿hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.li
hat_list[2] = int(input("ENter a number here: ..."))

# Step 2: write a line of code that removes the last element from the list.
del hat_list[-1]

# Step 3: write a line of code that prints the length of the existing list.
print("\nLength of the list is: ...", len(hat_list))

print(hat_list)
