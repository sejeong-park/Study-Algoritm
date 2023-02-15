# 2504 괄호의 값

array = list(input())

stack = []
result = 0
tmp = 1

for i in range(len(array)):

	if array[i] == '(':
		stack.append(array[i])
		tmp *= 2
	elif array[i] == '[' :
		stack.append(array[i])
		tmp *= 3
	elif array[i] == ')':
		if array[i-1] == '(':
			result += tmp
		if not stack or stack[-1] == '[':
			result = 0
			break
		stack.pop()
		tmp //= 2
	elif array[i] == ']':
		if array[i-1] == '[':
			result += tmp
		if not stack or stack[-1] == '(':
			result = 0
			break
		stack.pop()
		tmp //= 3
	print(stack, tmp, result)

if stack:
	print(0)
else:
	print(result)