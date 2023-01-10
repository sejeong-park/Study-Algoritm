# 이것이 코딩테스트이다 - 숫자 카드 게임

n, m = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(n)]

row_list = []
for i in range(n):
	row_list.append(min(cards[i]))

print(max(row_list))