import heapq
n = int(input())
# 힙에 초기 카드 묶음을 모두 삽입
heap = []
for i in range(n):
    data= int(input())
    heapq.heappush(heap, data)

result = 0
# 힙에 원소가 1개 남을 때까지
while len(heap) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    # 카드 묶음 합쳐서 다시 삽입
    sum_value = one + two
    result+=sum_value
    heapq.heappush(heap, sum_value)
print(result)

# 이렇게 푼건 왜 안돼?
# n = int(input())
# cards = []
# for _ in range(n):
#     each_card = int(input())
#     cards.append(each_card)
#
# cards.sort()
# total = cards[0]
# result = []
# for idx in range(1,len(cards)):
#     total+=cards[idx]
#     result.append(total)
#
# print(sum(result))