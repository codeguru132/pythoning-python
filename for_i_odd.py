for i in range(0,11):
    if i % 3 == 0:
        print(i)

print("Printing the while loop: ...")
        
x = 1

while x < 11:
    
    if x % 3 == 0:
        print(x)
    x += 1
        

for ch in "john.smith@ucu.ac.ug":
    if ch == '@':
        break
    print(ch, end="")

print()

print("Printing another for loop with continue...")



for di in "01542434002942101":
    if di == '0':
        
        di = 'x'
        
        
    print(di,end="")


print()
print("something different: ...")

for digit in "01542434002942101":
    if digit == '0':
        print("x", end="")
        continue
    print(digit, end="")





