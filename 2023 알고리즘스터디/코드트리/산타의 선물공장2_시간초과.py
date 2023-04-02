# 산타의 선물공장 2 - 시간초과 해결 (코드트리 해설지)

MAX_N = 100000
MAX_M = 100000

n, m, q = -1, -1, -1

# id에 해당하는 상자의 nxt 값과 prv 값을 관리한다. -> 0 이면 없다는 뜻
prv = [0] * (MAX_M + 1)
nxt = [0] * (MAX_M + 1)

# 각 벨트 별 head, tail id, 총 선물 수 관리
head = [0] * MAX_N
tail = [0] * MAX_N
num_gift = [0] * MAX_N

def build_factory(elements) :
	n, m = elements[1], elements[2] 		# 공장 정보를 입력 받는다.
	box_list = elements[3:]
	boxes = [[] for _ in range(n)]			# 벨트 정보를 만들어 준다.

	for index, box_num in enumerate(box_list) :
		boxes[box_num-1].append(index+1)

	# 초기 벨트의 head, tail, nxt, prv 값 설정
	for belt_num in range(n) :
		if len(boxes[belt_num]) == 0:
			continue

		head[belt_num] = boxes[belt_num][0]
		tail[belt_num] = boxes[belt_num][-1]

		# 벡트 내 선물 총 수 관리
		num_gift[belt_num] = len(boxes[belt_num])

		# nxt, prv 설정
		for i in range(len(boxes[belt_num]) - 1) :
			nxt[boxes[belt_num][i]] = boxes[belt_num][i+1]
			prv[boxes[belt_num][i+1]] = boxes[belt_num][i]

def move(elements) :
	m_src, m_dst = elements[1] - 1, elements[2] - 1

	# m_src에 물건이 없다면, m_dst내 물건 수가 답이 된다
	if num_gift[m_src] == 0 :
		print(num_gift[m_dst])
		return

	# m_dst에 물건이 없다면 그대로 옮겨 준다.
	if num_gift[m_dst] == 0 :
		head[m_dst] = head[m_src]
		tail[m_dst] = tail[m_src]
	else :
		orig_head = head[m_dst]
		# m_dst의 head를 교체해준다.
		head[m_dst] = head[m_src]
		# m_src의 tail과 기존 m_dst의 head를 연결해준다.
		src_tail = tail[m_src]
		nxt[src_tail] = orig_head
		prv[orig_head] = src_tail

	# head, tail을 비워준다.
	head[m_src], tail[m_src] = 0, 0

	# 선물 상자 수를 갱신해준다.
	num_gift[m_dst] += num_gift[m_src]
	num_gift[m_src] = 0

	print(num_gift[m_dst])

# 해당 벨트의 head를 제거한다.
def remove_head(b_num) :
	# 불가능 하다면 패스
	if not num_gift[b_num] :
		return 0

	# 노드가 1개라면, head, tail 모두 삭제 후 반환
	if num_gift[b_num] == 1:
		box_num = head[b_num]
		head[b_num], tail[b_num] = 0, 0
		num_gift[b_num] = 0		# 한개였다면 아예 없애준다.
		return box_num

	# head를 바꿔준다.
	hid = head[b_num]
	next_head = nxt[hid]
	nxt[hid], prv[next_head] = 0, 0
	num_gift[b_num] -= 1
	head[b_num] = next_head

	return hid

# 해당 벨트에 head를 추가한다.
def push_head(b_num, hid) :
	# 불가능한 경우 진행하지 않는다.
	if hid == 0 :
		return

	# 비어있었다면, head, tail이 동시에 추가
	if not num_gift[b_num] :
		head[b_num], tail[b_num] = hid, hid
		num_gift[b_num] = 1

	# 비어있지 않았다면, head만 교체
	else :
		orig_head = head[b_num]
		nxt[hid] = orig_head
		prv[orig_head] = hid

		head[b_num] = hid
		num_gift[b_num] += 1

def change(elements) :
	m_src, m_dst = elements[1] - 1, elements[2] - 1

	src_head = remove_head(m_src)
	dst_head = remove_head(m_dst)
	push_head(m_dst, src_head)
	push_head(m_src, dst_head)

	print(num_gift[m_dst])

def divide(elements) :
	m_src, m_dst = elements[1] - 1, elements[2] - 1

	cnt = num_gift[m_src]	# 순서대로 src에서 박스들을 빼준다.
	box_ids = []
	for _ in range(cnt//2) :
		box_ids.append(remove_head(m_src))

	# 거꾸로 뒤집어서 하나씩 dst에 박스들을 넣어준다.
	for i in range(len(box_ids) - 1, -1, -1) :
		push_head(m_dst, box_ids[i])

	print(num_gift[m_dst])

# 선물 점수를 얻는다.
def gift_score(elements) :
	p_num = elements[1]

	a = prv[p_num] if prv[p_num] != 0 else -1
	b = nxt[p_num] if nxt[p_num] != 0 else -1

	print(a + 2 * b)

# 벨트 정보를 얻는다.
def belt_score(elements) :
	b_num = elements[1] - 1

	a = head[b_num] if head[b_num] != 0 else -1
	b = tail[b_num] if tail[b_num] != 0 else -1
	c = num_gift[b_num]

	print(a + 2 * b + 3 * c)


q = int(input())
for _ in range(q) :
	elements = list(map(int, input().split()))
	q_type = elements[0]

	if q_type == 100 :
		build_factory(elements)
	elif q_type == 200 :
		move(elements)
	elif q_type == 300 :
		change(elements)
	elif q_type == 400 :
		divide(elements)
	elif q_type == 500 :
		gift_score(elements)
	else :
		belt_score(elements)