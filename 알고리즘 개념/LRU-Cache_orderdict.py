# LRU-Cache
# 자주 사용되는 데이터는 캐시에 남기고, 자주 사용되지 않는 캐시는 삭제해서 제한된 리소스 내에서 데이터를 빠르게 접근

from collections import OrderedDict

class LRUCache:
	def __init__(self, capacity):
		# 최대 캐시 크기
		self.capacity = capacity

		# 캐시 역할
		self.cache = OrderedDict()

	def get(self, key):
		if key not in self.cache:
			# 캐시의 키가 없으므로 return None
			return None
		else:
			# 캐시에 이미 존재
			# 사용되었으므로 캐시의 제일 뒤로 옮기기
			self.cache.move_to_end(key)
			return self.cache[key]

	def put(self, key, value):
		# 캐시에 추가, 캐시에 이미 존재했다면 value를 업데이트 수행
		self.cache[key] = value
		# 사용되었으므로 캐시의 제일 뒤로 옮기기
		self.cache.move_to_end(key)
		# 캐시 사이즈가 최대 크기가 넘어섰다면
		if len(self.cache) > self.capacity :
			# 가장 오랫동안 참조되지 않은 아이템을 캐시에서 제거
			self.cache.popitem(last = False)

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




