import sys
import copy
"""
지도의 각 칸에는 정수
# 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여있는 수가 칸에 복사된다.
# 0이 아닌 경우, 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다. 
# 주사위는 지도 바깥으로 이동할 수 없다. 만약 바깥으로 이동시켜고 하는 경우 해당 경우를 무시하고, 출력도 하지 않는다.
"""

input = sys.stdin.readline
n, m, x, y, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
move = list(map(int, input().split()))

# 가장 처음에 주사위는 모든 면에 0이 적혀있다.
dice = {
	"top" : 0
	, "bottom" : 0
	, "right" : 0
	, "left" : 0
	, "up" : 0
	, "down" :0
}

# 동, 서, 북, 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dice_move(d) :
	"""
	변경되는 주사위
	"""
	new_dice = copy.deepcopy(dice)

	# 동쪽으로 굴러갈때
	if d == 0 :
		new_dice["top"], new_dice["bottom"] = dice["left"], dice["right"]
		new_dice["right"], new_dice["left"] = dice["top"], dice["bottom"]

	# 서쪽으로 굴러갈때
	elif d == 1 :
		new_dice["top"], new_dice["bottom"] = dice["right"], dice["left"]
		new_dice["right"], new_dice["left"] = dice["bottom"], dice["top"]

	# 북쪽으로 굴러갈 때
	elif d == 2 :
		new_dice["top"], new_dice["bottom"] = dice["down"], dice["up"]
		new_dice["up"], new_dice["down"] = dice["top"], dice["bottom"]

	# 남쪽으로 굴러갈 때
	elif d == 3 :
		new_dice["top"], new_dice["bottom"] = dice["up"], dice["down"]
		new_dice["up"], new_dice["down"] = dice["bottom"], dice["top"]

	return new_dice

def change_array(x, y) :
	global array, dice

	# 이동한 칸에 쓰여 있는 수가 0이면
	if array[x][y] == 0 :
		array[x][y] = dice["bottom"] # 사위 바닥면에 쓰여 있는 수 복사
	else :
		dice["bottom"] = array[x][y] # 칸에 쓰여 있는 수가 주사위 바닥에 복사
		array[x][y] = 0 # 칸에 쓰인 수는 0


# 주사위기 움직인다.
for idx in move :

	direction = idx - 1 # 한개씩 줄어들면 줄어드는 방향으로 회전

	nx = x + dx[direction]
	ny = y + dy[direction]
	# 주사위는 지도 바깥으로 이동시킬 수 없다! -> 바깥으로 이동시키려고 하면, 해당 명령 무시하고 출력도 하지 않는다.
	if not (0<=nx<n and 0<=ny<m) :
		nx = x
		ny = y
		continue
	# 주사위의 이동갱신
	x, y = nx ,ny
	dice = dice_move(direction)

	# 주사위와 칸이 변경되는 부분
	change_array(x, y)

	# 주사위가 이동했을 때 마다 상단에 쓰여 있는 값
	print(dice["top"])
