import math

n, m = map(int, input().split())

def is_prime_number(x):
    # 만약 1이라면 소수가 아니므로 Falser 리턴
    if x == 1: return False
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

for idx in range(n, m+1):
    if is_prime_number(idx) == True:
        print(idx)

