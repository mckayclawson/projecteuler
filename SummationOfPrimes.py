def isPrime(num):
        isPrime = True
        if (num % 2) == 0:
                return False
        for x in range (2,num):
                if(num % x) == 0:
                        isPrime = False
                        break
        return isPrime

def generatePrimes():
        listOfPrimes = [2]
        counter = 3
        while(listOfPrimes[-1] < 2000000):
                if(counter % 10000) == 0:
			print counter
		if isPrime(counter):
                        listOfPrimes.append(counter)
                counter+=1
        return listOfPrimes[-1]

def main():
        print generatePrimes()

main()

