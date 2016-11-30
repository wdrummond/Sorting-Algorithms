import random

def listmaker():
	alist = []
	for i in range(21):
		num = random.randrange(100)
		alist.append(num)
	return alist

def selectionsort(l, checks):
	#print l
	for i in range(len(l)):
		smallest = i
		for j in range(i+1, len(l)):
			#compare increment
			checks[0] += 1
			if l[j] < l[smallest]:
				smallest = j
		l[i], l[smallest] = l[smallest], l[i]
		#swap increment
		checks[1] += 1
	#print l
	return checks

if __name__ == "__main__":
	A = listmaker()
	A2 = []
	for i in range(len(A)):
		A2.append(A[i])
	print A
	print A2
	C = selectionsort(A, [0,0])
	A2.sort()
	if A == A2:
		print "OK"
	print C