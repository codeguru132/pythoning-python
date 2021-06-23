blocks = int(input("Enter the number of blocks: "))

height = 0
#
# Write your code here.
#	
layers_between = 1
while layers_between <= blocks:
    height += 1
    blocks -= layers_between
    layers_between += 1
     

print("The height of the pyramid:", height)
