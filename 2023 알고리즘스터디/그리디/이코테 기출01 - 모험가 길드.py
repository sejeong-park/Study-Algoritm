# 이것이 코딩테스트이다 기출01 - 모험가 길드

n = int(input())
array = list(map(int, input().split()))
array.sort()

result = 0	# 그룹
cnt = 0

for i in array:
	cnt += 1
	if cnt >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
		result += 1
		cnt = 0	# 현재 그룹에 포함된 모험가의 수 초기화

print(result)
