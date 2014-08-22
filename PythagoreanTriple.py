'''
Author: McKay Clawson
Date 08/16/14
'''
def main():
	for b in range(1,1000):
		a = ((500000 - (1000*b))/(1000-b))
		c = 1000 - a - b
		if ((a*a) + (b*b) == (c*c)) and (a+b+c == 1000) and (a>0) and (b>0) and (c>0) and (c>b) and (b>a):
			print 'a is',a,'b is',  b,'c is', c, 'and their product is', a*b*c

main()
