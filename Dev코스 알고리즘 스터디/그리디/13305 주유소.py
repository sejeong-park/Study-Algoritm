

n = int(input())
distance = list(map(int, input().split()))
money = list(map(int, input().split()))

min_money = money[0]
result = 0

# 최소 비용
# 제일 가격이 낮은 주유소에서 기름 넣기
for i in range(n-1) :
	if min_money >= money[i] : # 가장 값이 싼 주유소가 현재 주유소보다 비싸면 변경
		min_money = money[i]

	result += min_money * distance[i]

print(result)