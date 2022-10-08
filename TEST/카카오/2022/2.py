from itertools import permutations
users = [[40,10000],[25,10000]]
emoticons = [7000,9000]


# users = [[40,2900], [23,10000],[11,5200],[5,5900],[40,3100],[27,9200],[32,6900]]
# emoticons = [1300,1500,1600,4900]

def solution(users, emotions) :
	answer = []

	discount_option = [10,20,30,40]

	emoticon_result = 0
	money_result = 0


	# 할인 율
	for discount in permutations(discount_option, len(emoticons)):
		user_list = dict()
		emoticon_money_max = []
		for user_id, user in enumerate(users):
			user_discount, user_money = user
			user_payment = 0
			# 이모티콘 카운트
			user_pay_list = {user_id : 0}
			for emo_id, emo_dis in enumerate(discount):
				emo_money = ((100-emo_dis)/100) * emoticons[emo_id]
				if emo_dis < user_discount:
					# print(user_id, user_payment)
					# #continue
				else:
					user_payment += emo_money
					print(user_id , user_payment)


		print('---')





	return answer

print(solution(users, emoticons))