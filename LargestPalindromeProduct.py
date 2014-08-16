'''
Author: McKay Clawson
Project Euler Problem 4
Date: 08/16/14
LargestPalindromeProduct
'''
			
def makePalindrome(firstHalf):
	stringNumber = str(firstHalf)
        listNumber = list(stringNumber)
	return int(listNumber[0] + listNumber[1] + listNumber[2] + listNumber[2] + listNumber[1] + listNumber[0])
			 
def main():
	firstHalf = 998
	palindrome = 0
	found = False
	
	while(not found):
		firstHalf-=1
		palindrome = makePalindrome(firstHalf)
		for x in range(99,999):
			if(palindrome / x < 99) or (x*x > palindrome):
				break
			if(palindrome % x) == 0 and palindrome / x < 999:
				found = True
				print x, palindrome, palindrome /x
main()	
