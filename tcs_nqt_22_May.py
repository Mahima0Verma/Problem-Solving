
l = [0,1]
def fib(n):
	while len(l) <= n:
		l.append(l[-1] + l[-2])
	return l[n]	
	
n = input()

try:

    n = int(n)
    if n<0:
        print("Invalid Input")
    else:
        print(l)		
        print(fib(n))
        print(l)
	      
except:
	print("Invalid Input")   	




