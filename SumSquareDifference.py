'''
Author: McKay Clawson
Date: 08/16/14
'''

def calculateSummation(num):
	counter = 1
	sum = 0
	while(counter <= num):
		sum += counter
		counter += 1
	return sum

def calculateSquareSummation(num):
	counter = 1
        sum = 0
        while(counter <= num):
                sum = sum + (counter*counter)
                counter += 1
        return sum

def main():
	#num = 10
	num = 100
	sequentialSum = calculateSummation(num)
	sequentialSumSquared = sequentialSum*sequentialSum
	squareSum = calculateSquareSummation(num)
	print sequentialSumSquared - squareSum
	

main()
