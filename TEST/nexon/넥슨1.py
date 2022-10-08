
samDaily = 100
kellyDaily = 100
difference = 0

def minNum(samDaily, kellyDaily, difference):
    # Write your code here
	samSolved = samDaily + difference
	kellySolved = kellyDaily
	cnt = 1
	while True:
		if difference == 0:
			return -1
		if samSolved < kellySolved:
			 return cnt

		samSolved += samDaily
		kellySolved += kellyDaily
		cnt+=1





	return "test"
print(minNum(samDaily, kellyDaily, difference))