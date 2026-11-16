text = input("Enter a string: ")

upper = 0
lower = 0

for i in text:
    if i >= 'A' and i <= 'Z':
        upper += 1
    elif i >= 'a' and i <= 'z':
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)