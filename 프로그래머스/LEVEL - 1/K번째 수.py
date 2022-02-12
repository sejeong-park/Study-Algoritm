# K 번째 수

array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]

def solution(array, command):
    answer = []
    for command in commands:
        sample = array[command[0]-1:command[1]]
        sample.sort()
        answer.append(sample[command[2]-1])

    return answer

print(solution(array, commands))