# 20055 - 컨테이너 벨트 위의 로봇
from collections import deque
n, k = map(int, input().split())
array = deque(list(map(int, input().split())))
robot = deque([0]*n)

result = 0

while True :
	array.rotate(1)
	robot.rotate(1)
	robot[-1] = 0 # 로봇이 내려가는 곳이니 0

	if sum(robot) :
		# 로봇이 내려가는 부분 인덱스가 i-1이므로, 그전인 i-2부터!
		for i in range(n-2, -1, -1) :
			if robot[i] == 1 and robot[i+1] == 0 and array[i+1] >= 1:
				robot[i+1] = 1 # 로봇 이동
				array[i+1] -= 1 # 내구성 하락
				robot[i] = 0 # 로봇 이동

		robot[-1] = 0 # 로봇 아웃
	# 올리는 위치에 내구도 0 아니면 로봇 올리기 &
	if robot[0] == 0 and array[0] >= 1 :
		robot[0] = 1
		array[0] -= 1

	result += 1	# round 수
	# 내구도 0인 칸 수가 k 이상이면 종료
	if array.count(0) >= k:
		break
print(result)



