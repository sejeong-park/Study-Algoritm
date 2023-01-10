# 2212 센서

n = int(input())
k = int(input())
# 센서의 좌표
sensors = list(map(int, input().split()))
print(sensors)
sensors.sort()
# 센서들의 위치를 오름차순으로 정렬 -> 고속도로에서 일직선으로 원점부터 위치에 놓여있기 때문
distance = []
for i in range(n-1):
	# 센서들 사이의 거리
	distance.append(sensors[i+1]-sensors[i])

distance.sort()
# 센서 사이의 거리가 가까운 센서들을 우선적으로 묶기 위함
# 거리가 서로 가까운 센서들을 우선적으로 묶기 위함
print(sum(distance[:n-k]))
# 앞에서부터 n-k를 더해준다는 것은 센서 간의 차이가 가장 큰 값을 k-1개 빼주는 것과 같다.
