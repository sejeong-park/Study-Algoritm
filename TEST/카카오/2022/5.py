from collections import deque
commands = ["UPDATE 1 1 menu", "UPDATE 1 2 category" , "UPDATE 2 1 bibimbap" ,
			"UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean",
			"UPDATE 3 3 noodle", "UPDATE 3 4 instant" , "UPDATE 4 1 pasta" , "UPDATE 4 2 italian",
			"UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik",
			"UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]

#commands = ["UPDATE 1 1 a" , "UPDATE 1 2 b" , "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
import sys

def bfs(ori,new) :
	queue = deque(ori)
	print(queue)

	return queue

def solution(commands) :
	answer = []
	array = [[""]*4 for _ in range(4)]
	keyword_dict, merge_dict_each, merge_dict_all = {}, {}, {}


	for command in commands:
		command_list = command.split()

		# UPDATE이면
		if command_list[0] == "UPDATE":
			# CASE1 일반 업데이트
			if len(command_list) == 4:
				r, c = int(command_list[1])-1, int(command_list[2])-1
				array[r][c] = command_list[-1]

				if command_list[-1] not in keyword_dict:
					keyword_dict[command_list[-1]] = []
				keyword_dict[command_list[-1]].append((r,c))	# 히스토리용

			# CASE2 대치 업데이트
			else:
				before, after = command_list[1], command_list[2]
				# merge에 속한 것이 있는 지
				print("MERGE 대치 : ", keyword_dict[before])
				for r,c in keyword_dict[before]:
					array[r][c] = after


					# if (r, c) in merge_dict_each.keys():
					# 	for idx, jdx in merge_dict_each[(r, c)]:
					# 		array[idx][jdx] = after

		############   	MERGE
		if command_list[0] == "MERGE":

			r1, c1, r2, c2 = command_list[1:]
			r1, c1, r2, c2 = int(r1)-1,int(c1)-1,int(r2)-1,int(c2)-1

			if r1 > r2 :
				r1, r2 = r2, r1
			if c1>c2:
				c1, c2 = c2, c1

			if (r2,c2) in merge_dict_each.keys():
				origin_list = merge_dict_each[(r2,c2)]
				r1, c1 = merge_dict_each[0]

			# 어떤 값으로 저장할 것인지
			if array[r1][c1] != "" and array[r2][c2] == "":
				target = array[r1][c1]
			elif array[r1][c1] == "" and array[r2][c2] != "":
				target = array[r2][c2]
			else:
				target = array[r1][c1]

			print('----')
			print(f"MERGE target :: {target}")

			# 반복문을 위해!
			if r1 > r2 :
				r1, r2 = r2, r1
			if c1>c2:
				c1, c2 = c2, c1

			merge_object = []
			for idx in range(r1,r2+1) :
				for jdx in range(c1, c2+1) :
					merge_object.append((idx,jdx))
					array[idx][jdx] = target # target 으로 쓰긴 씀
					# # 키워드 저장소에 대체 키워드가 있는 지 확인
					# if target in keyword_dict:
					# 	keyword_dict[target].append((idx,jdx))

			merge_dict_all[tuple(merge_object)] = merge_object

			for idx in merge_object:
				if idx in merge_dict_each:



		print("ARRAY : " , array)




	return answer

print(solution(commands))