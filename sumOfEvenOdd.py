n = int(input("Enter array size: "))

numbers = []

for i in range(n):
    value = int(input("Enter element: "))
    numbers.append(value)

even_sum = 0
odd_sum = 0

for i in numbers:
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i

print("Even sum:", even_sum)
print("Odd sum:", odd_sum)