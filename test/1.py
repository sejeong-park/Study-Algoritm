
T = int(input())

for t in range(T) :
	n = int(input())
	array = list(map(int, input().split()))
	cnt = 0
	# 기준점이 되는 i
	for i, num in enumerate(array) :
		# num이 양수이면
		if num > 0 and i+num < len(array):
			if num + array[i+num] == 0:
				cnt += 1
				array[i+num] = 0 # 없는 것으로 변경

		# num이 음수 이면
		if num < 0 and i-num < 0 :
			if num + array[i-num] == 0:
				cnt += 1
				array[i-num] = 0

	print(f"#{t+1} {cnt}")



