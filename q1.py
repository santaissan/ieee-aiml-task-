n = int(input("how many no.? "))
nums = list(map(int, input("enter them with space: ").split()))

big = nums[0]
small = nums[0]
total = 0
even = 0
odd = 0

for x in nums:
    if x > big:
        big = x
    if x < small:
        small = x
    total = total + x
    if x % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1


rev = []
i = len(nums) - 1
while i >= 0:
    rev.append(nums[i])
    i = i - 1

print("Largest:", big)
print("Smallest:", small)
print("Sum:", total)
print("Even count:", even)
print("Odd count:", odd)
print("Reversed:", *rev)