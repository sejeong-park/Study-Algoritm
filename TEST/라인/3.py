from typing import List

n= 3
m = 2
fires = [[1,1]]
ices = [[3,3]]

def fire_totem(array, fires, m) :

	for fire in fires:
		x, y = fire[0] , fire[1]
		for idx in range(x-m, x+m):
			for jdx in range(y-m, y+m):
				if 0<= idx <= len(array[0]) and 0<= jdx <= len(array[1]) :
					array[idx][jdx] += 1
	return array


def solution(n: int, m: int, fires: List[List[int]], ices: List[List[int]]) -> List[List[int]]:
	answer = [[]]
	array = [[0]*n for _ in range(n)]
	count = 0
	for _ in range(m):
		fire_totem(array, fires, m)
	return array

solution(n, m, fires, ices)
print(solution(n,m,fires,ices))