from collections import deque
cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]


def solution(cacheSize, cities):
	answer = 0
	cache = deque(maxlen = cacheSize)
	if cacheSize == 0:
		return len(cities) * 5

	for city in cities:
		city = city.lower()		# 대소문자 구분하지 않기 위해 모두 소문자로 변경
		# 캐시에 있는 데이터라면
		if city in cache :
			answer += 1
			cache.remove(city)
		# 캐시에 없는 데이터라면
		else:
			answer += 5
		cache.append(city)

	return answer

print(solution(cacheSize, cities))
