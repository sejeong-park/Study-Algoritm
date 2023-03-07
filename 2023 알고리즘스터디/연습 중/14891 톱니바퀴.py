# 14891 - 톱니바퀴
from collections import deque
array = {}
for i in range(1,5):
	array[i] = deque((map(int, input())))

k = int(input())

# 오른쪽 방향
def rotate_right(num, direction):
	if num > 4 or array[num - 1][2] == array[num][6]:
		return
	if array[num-1][2] != array[num][6]:
		rotate_right(num+1, -direction)
		array[num].rotate(direction)

# 왼쪽 방향
def rotate_left(num, direction):
	if num < 1  or array[num+1][6] == array[num][2]:
		return
	if array[num+1][6] != array[num][2]:
		rotate_left(num-1, -direction)
		array[num].rotate(direction)

for _ in range(k):
	num, direction = map(int, input().split())

	rotate_right(num+1, -direction)
	rotate_left(num-1, -direction)
	array[num].rotate(direction)


result, cnt = 0, 0
for key, value in array.items():
	result += value[0] * (2**(key-1))

print(result)
