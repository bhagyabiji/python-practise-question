n = int(input("Enter array size: "))

numbers = []

for i in range(n):
    value = int(input("Enter element: "))
    numbers.append(value)

smallest = numbers[0]

for i in numbers:
    if i < smallest:
        smallest = i

print("Smallest element:", smallest)