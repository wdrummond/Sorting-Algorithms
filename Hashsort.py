import random

def listmaker():
	alist = []
	for i in range(21):
		num = random.randrange(20)
		alist.append(num)
	return alist

def hashsort(l, checks):
	size = len(l)
	frequency = [0]*size
	for i in range(size):
		value = l[i]
		frequency[value] += 1
	p = 0
	for i in range(size):
		for j in range(frequency[i]):
			l[p] = i
			p += 1
# for keeping record
	checks[0] = size
	checks[1] = size
	return checks
		
	
		





if __name__ == "__main__":
	A = listmaker()
	A2 = []
	for i in range(len(A)):
		A2.append(A[i])
	print A
	print A2
	C = hashsort(A, [0,0])
	A2.sort()
	if A == A2:
		print "OK"
	print C