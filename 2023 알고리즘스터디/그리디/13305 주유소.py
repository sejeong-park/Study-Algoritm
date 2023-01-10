# 13305 주유소

n = int(input())
distance = list(map(int, input().split()))
money = list(map(int, input().split()))

min_money = money[0]			# 첫번재 도시의 가격
result = 0

for i in range(n-1):
	# 현재 최소 금액보다 다음 도시의 리터값이 더 저렴할 때
	if min_money >= money[i]:
		min_money = money[i]

	result += min_money * distance[i]


print(result)
