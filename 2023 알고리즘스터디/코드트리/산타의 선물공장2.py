# 코드트리 - 산타의 선물공장 2
import sys
from collections import deque

total_factory = []
def build_factory(input_list) :
	"""
	n, m, b_num1, b_num2, ... b_num_m
	"""
	n, m, box_list = input_list[0], input_list[1], input_list[2:]

	total_factory = [deque([]) for _ in range(n+1)]	# 순서 그대로 하기 위함

	for index, box_num in enumerate(box_list) :
		total_factory[box_num].append(index + 1)	# 인덱스는 +1

	return total_factory

def move_object(m_src, m_dst) :
	"""
	m_src번째 벨트에 있는 선물들을 모두 m_dst번째 벨트의 선물들로 옮긴다.
	옮겨진 벨트들은
	return : m_dst의 선물의 총 수를 출력
	"""
	while total_factory[m_src] :
		box_num = total_factory[m_src].pop()
		total_factory[m_dst].appendleft(box_num)

	print(len(total_factory[m_dst])) 				# 출력값
	return total_factory

def change_object_first(m_src, m_dst):
	"""
	m_src번째 선물 중 가장 앞에 있는 선물을 m_dst번째 벨트의 선물들 중 가장 앞에 있는 선물과 교체!
	-> 둘 중 하나의 벨트에 서눔ㄹㅇ 아예 존재하지 않는다면, 해당 벨트로 선물을 옮기기만한다.
	-> 옮긴 뒤 m_dist번째 벨트에 있는 선물들의 개수
	return : m_dst의 선물의 총 수
	"""
	if len(total_factory[m_src]) == 0 and len(total_factory[m_dst]) == 0 :
		pass
	elif len(total_factory[m_src]) == 0 :
		box_num = total_factory[m_dst].popleft()
		total_factory[m_src].appendleft(box_num)
	elif len(total_factory[m_dst]) == 0 :
		box_num = total_factory[m_src].popleft()
		total_factory[m_dst].appendleft(box_num)
	else :
		box_src = total_factory[m_src].popleft()
		box_dst = total_factory[m_dst].popleft()
		total_factory[m_dst].appendleft(box_src)
		total_factory[m_src].appendleft(box_dst)

	print(len(total_factory[m_dst]))
	return total_factory

def divide_object(m_src, m_dst):
	"""
	return : m_dst의 선물의 총 수
	해당 명령은 최대 100번까지만 주어진다.
	"""
	n = len(total_factory[m_src])
	if n != 1 :
		for _ in range(n//2) :
			box_num = total_factory[m_src].popleft()
			total_factory[m_dst].appendleft(box_num)

	print(len(total_factory[m_dst]))
	return total_factory

def get_object_info(p_num) :
	"""
	return : 앞 선물의 번호 a와 뒤 선물의 번호 b -> a + 2b
	"""
	a, b = -1, -1
	for belt_num in range(1, len(total_factory)) :
		queue = list(total_factory[belt_num])
		for index, box_num in enumerate(queue) :
			if p_num == box_num :
				# 앞 선물이 있는 경우
				if index - 1 >= 0 :
					a = queue[index-1]
				# 뒤 선물이 있는 경우
				if index + 1 < len(queue) :
					b = queue[index+1]
				break
	print(a + 2 * b)


def get_belt_info(b_num) :
	"""
	return : 앞 선물의 번호 a, 뒤 선물의 번호 b, 해당 벨트에 있는 선물의 개수 c -> a + 2b + 3c
	(a, b 없을 경우 -1, c 없을 경우 0)
	"""

	a, b, c = -1, -1, len(total_factory[b_num])
	if c != 0:
		a = total_factory[b_num][0]
		b = total_factory[b_num][-1]
	print(a + 2 * b + 3 * c)


input = sys.stdin.readline
q = int(input())	# 명령의 수
# 명령의 정보
for _ in range(q) :
	input_list = list(map(int, input().split()))
	q_num, q_input = input_list[0], input_list[1:]
	if q_num == 100 :
		total_factory = build_factory(q_input)	# factory 값 넣어주기
	elif q_num == 200 :
		total_factory = move_object(q_input[0], q_input[1])
	elif q_num == 300 :
		total_factory = change_object_first(q_input[0], q_input[1])
	elif q_num == 400 :
		total_factory = divide_object(q_input[0], q_input[1])
	elif q_num == 500 :
		get_object_info(q_input[0])
	elif q_num == 600 :
		get_belt_info(q_input[0])
