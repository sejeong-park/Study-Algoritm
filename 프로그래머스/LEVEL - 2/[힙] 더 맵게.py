import heapq

def solution(scoville, k):
    answer = 0

    heap = []
    for food in scoville:
        heapq.heappush(heap, food)
    # 힙의 최솟값이 k보다 크거나 같을 때 까지 반복
    while heap[0]<k:
        if len(heap)<=1:
            answer = -1
            break

        first = heapq.heappop(heap)
        second = heapq.heappop(heap)

        new = first + (second*2)

        heapq.heappush(heap, new)
        answer+=1

    return answer

scoville = [1,2,3,9,10,12]
k = 7
print(solution(scoville, k))