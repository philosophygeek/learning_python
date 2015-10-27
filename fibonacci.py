# This program will calculate the Fibonacci sequence in 3 different ways


GoldenRatio = (1.0 + (5.0**.5)) / 2.0
Psi = (1.0 - (5.0**.5)) / 2.0


def Fib_Recursive(n):
	if n == 1 or n == 2:
		return 1
	else:
		return Fib_Recursive(n-1) + Fib_Recursive(n-2)

def Fib_Straight(n):
	return ((GoldenRatio**n)-(Psi**n))/5**.5

def Fib_Iterative(n):
	f1 = 1
	f2 = 1
	if n == 1 or n == 2:
		return 1
	else: 
		for x in range (2, n):
			m = f1 + f2
			f1 = f2
			f2 = m
		return m

print "This program will calculate the nTh Fibonacci number."
print "First, pick an N."
N =int(raw_input("-> "))

recursive_soln = Fib_Recursive(N)
straight_soln = Fib_Straight(N)
iterative_soln = Fib_Iterative(N)

print "This is the %sth Fibonacci number calculated recursively: %r" % (N , recursive_soln) 
print "This is the %sth Fibonacci number calculated directly: %i" % (N , straight_soln)
print "This is the %sth Fibonacci number calculated iteratively: %r" % (N , iterative_soln)
