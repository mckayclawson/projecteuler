'''
Author: McKay Clawson
Project Euler Problem 5
Smallest Multiple
Date: 08/16/14
'''
def isCommonMultiple(num):
	checkList = [11,12,13,14,15,16,17,18,19,20]
	for x in checkList:
		if num % x != 0:
			return False
	return True


def main():
	found = False
	counter = 2520
	while(not found):
		if isCommonMultiple(counter):
			found = True
		else:
			counter+=2	
	print counter

main()
