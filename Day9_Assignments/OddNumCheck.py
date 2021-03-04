def isOddNum(num):
	if num % 2 == 0 and num > 0:
		return False
	elif num % 2 != 0 and num > 0:
		return True
	elif num < 0:
		return "Negative Numbers are not allowed"