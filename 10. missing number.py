nums = list(map(int, input("Enter numbers: ").split()))
n = len(nums) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)
missing = expected_sum - actual_sum
print("Missing number:", missing)