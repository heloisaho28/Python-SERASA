nums = []
dentro = fora = 0
n = int(input())

for i in range(0, n):
    nums.append(int(input()))

for i in nums:
    if 10 <= i <= 20:
        dentro += 1
    else:
        fora += 1

print(f"{dentro} in")
print(f"{fora} out")