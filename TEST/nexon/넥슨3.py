#[1, 2, 5] [2, 5, 4] 3
initial_players = [1, 2, 5]
new_players = [2, 5, 4]
rank = 3

def getMinimumHealth(initial_players, new_players, rank):

	total_health = 0
	cnt = 0
	while True:
		if cnt == 1 + len(new_players):
			break

		sort_list = list(set(initial_players))
		sort_list.sort(reverse=True)
		total_health += sort_list[rank-1]
		print(sort_list)
		print(initial_players)
		cnt += 1
		initial_players = initial_players + new_players[:cnt]

	return total_health

print(getMinimumHealth(initial_players, new_players, rank))
