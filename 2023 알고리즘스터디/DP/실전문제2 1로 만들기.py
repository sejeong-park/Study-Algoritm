# 이코테 실전 문제 2 - 1로 만들기

x = int(input())

d = [0] * 30001


for i in range(2, x+1) : # 2부터 x까지 반복
	d[i] = d[i-1] + 1

	if i % 2 == 0:
		d[i] = min(d[i] , d[i//2] + 1)

	if i % 3 == 0:
		d[i] = min(d[i] , d[i//3] + 1)

	if i % 5 == 0:
		d[i] = min(d[i] , d[i//5] + 1)

	print(i, d[i])

# 점화식 끝에 1을 더해주는 이유는 함수의 호출 횟수를 구해야 하기 때문
print(d)
print(d[x])