i = 0
j = not i
print("Zero is 'False'\nSo not 'False' is 'True'\nas seen below\n\n ")
print(j, end="\n")


k = 0
h = not not k
print("Not 'Zero' is 'True'\n So not 'True' is 'False'\as seen below\n\n")
print(h)


a = 1
b = not a
print(b)


c = 1
d = not not c
print(d)


print("""In summary, 0 represents 'FALSE' in logical operators and 1 represents 'TRUE'\n so 'not 0' gives us 'TRUE' and 'not TRUE' gives us 'FALSE'""")


g = 0o1111
f = 0o10110

print("Testing the working of logical 'and'")

log = g and f
print(log)
