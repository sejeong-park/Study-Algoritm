# 14916 거스름돈

coin = int(input())
cnt = 0
while True:
	if coin % 5 == 0:
		cnt += coin // 5
		break
	else:
		coin -= 2
		cnt += 1
	if coin < 0:
		break


if coin <0 :
	print(-1)
else:
	print(cnt)
