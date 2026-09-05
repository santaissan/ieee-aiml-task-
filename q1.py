n = int(input("enter no. of element: "))
numbers = list(map(int, input("enter the no separated by spaces: ").split()))

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num

total = 0
for num in numbers:
    total += num

even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

reversed_list = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Largest:", largest)
print("Smallest:", smallest)
print("Sum:", total)
print("Even count:", even_count)
print("Odd count:", odd_count)
print("Reversed:", *reversed_list)