import sys

file_path = sys.argv[1]

with open(file_path, "r", encoding="utf-8") as file:
    nums = [int(line) for line in file if line.strip()]

nums.sort()
median = nums[len(nums) // 2]
moves = sum(abs(num - median) for num in nums)

if moves <= 20:
    print(moves)
else:
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу")