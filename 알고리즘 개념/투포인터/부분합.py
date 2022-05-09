import sys
n, s = map(int, input().split())
array = list(map(int, input().split()))

end, total = 0, 0
min_value = n
for start in range(n):
    while end < n and total < s:
        total += array[end]
        end += 1
    if total >= s:
        min_value = min(min_value, end-start)
    total -= array[start]

if min_value == n:
    print(0)
else:
    print(min_value)