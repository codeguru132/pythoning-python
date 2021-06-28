my_list = [10, 1, 8, 3, 5] # list is assigned a sequence og five integer values
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)


#modified for loop

totals = 0
for j in my_list:
    totals += j
    
print(totals)