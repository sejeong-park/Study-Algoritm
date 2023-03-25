import sys
import copy

input = sys.stdin.readline


"""
output - 술래가 k번 턴 동안 얻게 되는 총 점수
술래 - 정 중앙에 서있다.
m 명의 도망자 / 도망자의 유형 - 상하로만 움직임(아래가 시작) & 좌우로만 움직임(오른쪽이 시작)
h 개의 나무 -> 도망자와 초기에 겹쳐져 주어지는 것 가능
1. m 명의 도망자가 먼저 동시에 움직인다.
2. 술래가 움직인다.
1~2 k번 반복
도망자가 움직일 때, 현재 술래와의 거리가 3 이하인 도망자만 움직인다.
-> 술래와의 거리가 3 이하인 도망자들 (1턴 동안의 규칙)
	- 현재 바라보고 있는 방향으로 1칸 움직인다 했을 때 격자를 벗어나지 않는 경우
		- 움직이려는 칸에 술래가 있는 경우라면, 움직이지 않는다.
		- 움직이려는 칸에 술래까지 있지 않다면 해당 칸으로 이동한다. -> 나무 있어도 OK
	- 현재 바라보고 있는 방향으로 1칸 움직일 때 -> 격자 밖
		- 방향 반대로 튼다.
		- 술래가 없다면 1칸 앞으로 이동한다.
"""