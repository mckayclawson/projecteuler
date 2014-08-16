
def isPrime(num):
        isPrime = True
        if (num % 2) == 0:
                return False
        for x in range (2,num):
                if(num % x) == 0:
                        isPrime = False
                        break
        return isPrime

def generate10001Primes():
        listOfPrimes = [2]
        counter = 3
	while(len(listOfPrimes) < 10001):
                if isPrime(counter):
                        listOfPrimes.append(counter)
		counter+=1
        return listOfPrimes[10000]

def main():
	print generate10001Primes()

main()
