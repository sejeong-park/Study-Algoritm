import requests
import json

country = "Puerto Rico"
phoneNumber = "564593986"

# Puerto Rico
# 564593986
def getPhoneNumbers(country, phoneNumber):
	print(country, phoneNumber)
	url = f'https://jsonmock.hackerrank.com/api/countries?name=Afghanistan'
	requestData = requests.get(url).json()["data"]

	if len(requestData) == 0:
		return -1
	else:
		print(requestData)
		requestData = requestData[0]
		if len(requestData["callingCodes"]) == 1:
			calling_code = requestData["callingCodes"][0]
		else:
			calling_code = requestData["callingCodes"][-1]

		return f"+{calling_code} {phoneNumber}"



print(getPhoneNumbers(country, phoneNumber))