n = int(input())
array = []
for _ in range(n):
    a =int(input())
    array.append(a)
array.sort(reverse=True)
for idx in array:
    print(idx)