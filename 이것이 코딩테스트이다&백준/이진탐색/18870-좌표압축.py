import sys
n = int(input())
array = list(map(int, input().split()))
array2 = list(sorted(set(array)))

dic =  {array2[i] : i for i in range(len(array2))}
# print(dic)
for i in array:
    print(dic[i], end = ' ')