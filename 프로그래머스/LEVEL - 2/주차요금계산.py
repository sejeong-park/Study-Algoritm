import math
fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]

def solution(fees, records):
	answer = []
	data = dict()
	for idx in records:
		time, car_num, type = idx.split()
		h, m = time.split(':')
		time_range = int(h)*60 + int(m)

		if car_num not in data:
			data[car_num] = {"IN" : [],"OUT" : []}
		if type == "IN":
			data[car_num]["IN"].append(time_range)
		else:
			data[car_num]["OUT"].append(time_range)
	data = sorted(data.items())
	for car_num, value in data:
		if len(value["IN"]) != len(value["OUT"]):
			value["OUT"].append(23*60 + 59)
		total_time = 0
		for car_in, car_out in zip(value["IN"], value["OUT"]):
			total_time += car_out - car_in
		#print(car_num, total_time)

		if total_time <= fees[0]:
			answer.append(fees[1])
		else:
			result = fees[1] + (math.ceil((total_time - fees[0]) / fees[2])) * fees[3]
			answer.append(result)
	return answer

print(solution(fees, records))