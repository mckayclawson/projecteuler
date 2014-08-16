import math

def isPrime(num):
	isPrime = True
	if (num % 2) == 0:
		return False
	for x in range (2,num):
		if(num % x) == 0:
			isPrime = False
			break
	return isPrime

def runPrimeTest():
	for y in range (2, 400):
		if isPrime(y):
			print y

def generateAllPrimes(num):
	listOfPrimes = []
	for x in range(2,num):
		if isPrime(x):
			listOfPrimes.append(x)
	return listOfPrimes

def generateAllNonEvenFactors(num):
	listOfFactors = []
        for x in range(2,num):
		if((num % x == 0) and (x % 2 == 1)):
			listOfFactors.append(x)
        return listOfFactors

def calculatePrimeFactors(listOfFactors,num):
	listOfPrimeFactors = []
	for x in listOfFactors:
		if(isPrime(x)):
			listOfPrimeFactors.append(x)
	return listOfPrimeFactors
	'''
	listOfPrimeFactors = []
	for x in listOfPrimes:
		if num % x == 0:
			listOfPrimeFactors.append(x)
	return listOfPrimeFactors
	'''
def calculateMaxPrimeFactor(listOfPrimeFactors):
	if len(listOfPrimeFactors) == 0:
		return 0
	max = listOfPrimeFactors[0]
	for x in range(0, len(listOfPrimeFactors)):
		if listOfPrimeFactors[x] > max:
			max = listOfPrimeFactors[x]
	return max

def main():
	#number = 600851475143
	number = 13195
	listOfFactors = generateAllNonEvenFactors(number)
	listOfPrimeFactors = calculatePrimeFactors(listOfFactors, number)
	for x in range(0,len(listOfPrimeFactors)):
		print str(listOfPrimeFactors[x]) + ' is a prime factor of ' + str(number)
	print listOfPrimeFactors
	print 'The largest prime factor of ' + str(number) + ' is ' + str(calculateMaxPrimeFactor(listOfPrimeFactors))

main()




