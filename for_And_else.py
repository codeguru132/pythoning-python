for i in range(5):
    print(i)
else:
    # i retains its last value
    print("else:", i)

# here the for is not even executed    
j = 111
for j in range(2,1):
    print(j)
else:
    print("else:", j)


