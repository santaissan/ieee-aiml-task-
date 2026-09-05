def process_list(numbers):
    result = numbers.copy()  

    for i in range(len(result) - 1, -1, -1):
        if result[i] < 0:
            result.remove(result[i])

    result.append(0)
    result.sort()

    return result
original = [5, -2, 8, -1, 3]
result = process_list(original)
print("Original:", original)
print("Result:", result)