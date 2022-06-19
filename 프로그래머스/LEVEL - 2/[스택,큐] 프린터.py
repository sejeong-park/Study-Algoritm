from collections import deque
priorities = [2,1,3,2]
location = 2

def solution(priorities, location):
    answer = 0
    queue  = deque([(data, idx) for idx, data in enumerate(priorities)])

    while len(queue):
        priority, index = queue.popleft()
        if queue and max(queue)[0] > priority:
            queue.append((priority, index))
        else:
            answer += 1
            if index == location:
                break
    return answer
print(solution(priorities, location))