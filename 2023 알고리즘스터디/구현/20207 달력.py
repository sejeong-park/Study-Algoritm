# 20207 - 달력

n = int(input())
calendar = [0] * 367	# 맨 앞 0은 그냥 무시 (어차피 날짜니까)

for _ in range(n):
	start, end = map(int, input().split())
	for i in range(start, end+1) :
		calendar[i] += 1

result = 0	# 결과

width = 0
height = 0
# 365개로 총 결과를 더하면, 365번째 날 결과가 카운팅되지 않는 반례가 존재
# 따라서 index 0 + 365 + 마지막 카운트용 = 총 367개 -> 마지막에는 무조건 0을 확인하여, result에 최종일자까지 계획을 확인하기 위함
for i in range(367):
	if calendar[i] != 0:
		width += 1  # 길이가 있을 때까지 찾기
		height = max(height, calendar[i])
	else:
		result += width * height
		width, height = 0,0

print(result)

