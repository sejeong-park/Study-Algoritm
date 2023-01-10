# 13164 - 행복 유치원
n, k = map(int, input().split())
kid_list = list(map(int, input().split()))

array = []
for i in range(n-1):
	array.append(kid_list[i+1] - kid_list[i])

array.sort(reverse = True)
print(sum(array[k-1:]))