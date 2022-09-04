def solution(m, musicinfos):
	answer = []
	time_list = []
	m = m.replace('A#', 'X').replace('C#', 'Y').replace('D#', 'Z').replace('G#', 'V').replace('F#', 'W')
	for music in musicinfos:
		start_time, end_time, title, melody = music.split(',')

		start_time = int(start_time.split(':')[0]) * 60 + int(start_time.split(':')[1])
		end_time = int(end_time.split(':')[0]) * 60 + int(end_time.split(':')[1])

		total_time = end_time - start_time

		melody = melody.replace('A#', 'X').replace('C#', 'Y').replace('D#', 'Z').replace('G#', 'V').replace('F#', 'W')

		count = total_time // len(melody) + 1 if total_time % len(melody) != 0 else total_time // len(melody)
		melody = str(melody * count)[: total_time]

		if m in melody:
			answer.append([title, total_time, start_time])

	if len(answer) == 0:
		return "(None)"
	elif len(answer) == 1:
		return answer[0][0]
	else:
		# data_list.sort(key=lambda x : len(x))
		answer.sort(key=lambda x: (-x[1], x[2]))
		return answer[0][0]