from itertools import permutations
numbers = [6,10,2]
def solutions(numbers):
    answer = 0
    numbers = list(map(str, numbers))
    # 인자 각각의 문자열을 3번 반복한다
    numbers.sort(key = lambda x:x*3, reverse = True)

    return str(int(''.join(numbers)))

print(solutions(numbers))