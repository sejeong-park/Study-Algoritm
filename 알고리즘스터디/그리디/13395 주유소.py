# 주유소

n = int(input())
distance = list(map(int, input().split()))
prices = list(map(int, input().split()))


min_price = prices[0]	# 최솟값을 첫번째 도시의 리터 당 가격으로 초기화
result  = 0

# 어차피, 가장 오른쪽에 있는 도시의 "리터 당 가격"은 고려되지 않게 됨 -> 추가 적인 블록이 없으니!
for i in range(n-1):
	if min_price >= prices[i]:	# 첫번째 도시보다 가격이 작을 경우, 최소 가격 갱신
		min_price = prices[i]
	result += min_price * distance[i]	# 한바퀴 돌때마다 최소 가격 곱해서 저장


print(result)