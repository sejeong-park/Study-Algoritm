class LRUCache :
	def __init__(self, capacity):
		# 최대 캐시 크기
		self.capacity = capacity

		# 캐시 역할
		self.cache = dict()

	def get(self, key):
		value = self.cache.get(key, None)
		if value :
			# 캐시에 존재 했다면, 삭제하고 뒤에 추가
			del self.cache[key]
			self.cache[key] = value

		return value

	def put(self, key, value):
		# 캐시에 이미 존재한다면 삭제
		if key in self.cache:
			del self.cache[key]

		# 캐시에 추가
		self.cache[key] = value

		# 캐시 사이즈가 최대 크기가 넘어섰다면
		if len(self.cache) > self.capacity:
			# 가장 오랫동안 참조되지 않은 아이템을 캐시에서 제거
			first_item_key = next(iter(self.cache))
			del self.cache[first_item_key]

cache = LRUCache(capacity = 3)
print(cache.cache)

cache.put(1,1)
print(cache.cache)
cache.put(2,2)
print(cache.cache)
cache.put(3,3)
print(cache.cache)
cache.get(1)
print(cache.cache)
cache.get(3)
print(cache.cache)
cache.put(4,4)
print(cache.cache)
cache.put(5,5)
print(cache.cache)


