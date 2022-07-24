from collections import deque

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    time = 0
    while bridge:
        time += 1
        bridge.pop(0)  # 다리 건너기
        if truck_weights:
            if truck_weights[0] + sum(bridge) <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

        print(bridge)

    return time

print(solution(bridge_length, weight, truck_weights))