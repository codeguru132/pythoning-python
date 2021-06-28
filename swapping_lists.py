my_list = [10,1,18,3,5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
print(my_list)
#works just fine for 5 elements. whatif they are 100

#CASE 2
new_list = [20,1,5,34,9]
length = len(new_list)

for j in range(length // 2):
    new_list[j], new_list[length - j -1] = new_list[length -j -1], new_list[j]

print(new_list)