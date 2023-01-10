# 이것이 코딩 테스트이다 02 - 실전 문제

n, m, k = list(map(int, input().split()))
array = list(map(int, input().split()))

array.sort(reverse = True)
first = array[0]
second = array[1]
# 반복되는 수열
# [6 6 6 5] -> (k+1)
cnt = int(m / (k+1)) * k
cnt += m % (k+1)

result = 0
result += (cnt)* first # 가장 큰 수 더하기
result += (m-cnt) * second # 두번째로 큰 수 더하기

print(result)


