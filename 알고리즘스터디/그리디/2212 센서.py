n = int(input())
k = int(input())
sensors = list(map(int, input().split()))
sensors.sort()

distance = []
for i in range(0, n-1):
	distance.append(sensors[i+1] - sensors[i])

distance.sort()
# print(distance)
# print(n-k)
print(sum(distance[:n-k]))