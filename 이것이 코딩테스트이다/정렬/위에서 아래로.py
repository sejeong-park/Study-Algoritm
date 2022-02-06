n = int(input())
n_list = []
for _ in range(n):
    n_list.append(int(input()))

n_list.sort(reverse=True)

for i in n_list:
    print(i, end = " ")