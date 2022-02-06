n = int(input())
array = []
for i in range(n):
    name, score = input().split()
    array.append([name, int(score)])

array.sort(key = lambda x : x[1])

for name, score in array:
    print(name, end = " ")