# 2212 - 센서 [골드 5]

n = int(input())
k = int(input())
sensor = list(map(int, input().split()))
sensor.sort()

print(sensor)

array = []
for i in range(0, n-1):
	array.append(sensor[i+1] - sensor[i])
print(array)
array.sort()
print(array)
print(n-k)
print(sum(array[:n-k]))

