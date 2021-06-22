largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end the program"))
    # this will make the while loop false
    # like if we put -1 the break will terminate the loop
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number
        

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")