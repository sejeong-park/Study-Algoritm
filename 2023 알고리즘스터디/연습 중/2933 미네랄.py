# 2933 미네랄 - 아 미친듯이 어렵네 ;;;;;';;;;;

r, c = map(int, input().split())
array = [list(input()) for _ in range(r)]	# 미네랄 집합
# . : 빈칸 / x : 미네랄
n = int(input()) # 횟수
height = list(map(int, input().split()))

def find_4way(x, y):
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]




def gravity():
	for j in range(c) : # 가로
		empty = 0
		for i in range(r-1, -1, -1):
			if array[i][j] == '.':
				empty +=1
			else:
				if i + empty != i :
					array[i + empty][j] = array[i][j]
					array[i][j] = '.'


def remove(line, start, end, cnt):
	for i in range(start, end, cnt):
		# 미네랄이 깨질때
		if line[i] == 'x' :
			line[i] = '.'
			gravity()
			break
	return line

# 막대기를 던지는 턴
def turn(direction, h):
	# 왼쪽 -> 오른쪽
	if direction == 0:
		array[h] = remove(array[h], 0, c, 1)
	else:
		array[h] = remove(array[h], c-1, -1, -1)

# 번갈아가는 횟수
for num in range(n):
	h = height[num]
	turn(num%2, r-h)
	print(array)

