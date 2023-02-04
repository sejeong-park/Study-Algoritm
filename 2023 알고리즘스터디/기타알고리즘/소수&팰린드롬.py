

def is_Prime(n):
	if n == 1:
		return False

	for i in range(2, int(n**0.5)+1):
		if not n%i :
			return False
	return True

def P_reverse(n):
	x = str(n)
	for i in range(len(x)//2):
		# 거꾸로 뒤집기
		if x[i] != x[-i-1]:
			return False
	return True

n = int(input())
while True:
	if is_Prime(n) and P_reverse(n):
		break
	n+=1

print(n)



