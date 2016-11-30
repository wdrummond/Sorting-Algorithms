import random
from Listmaker import *

def mergesort(l, checks):
	if len(l) <= 1:
		return
	left = l[:len(l)/2]
	right = l[len(l)/2:]
	mergesort(left, checks)
	mergesort(right, checks)
	lcount = 0
	rcount = 0
	mainlist = 0
	while lcount < len(left) and rcount < len(right):
		#compare increment
		checks[0] += 1
		if left[lcount] < right[rcount]:
			l[mainlist] = left[lcount]
			#swap increment
			checks[1] += 1
			lcount += 1
		else:
			l[mainlist] = right[rcount]
			#swap increment
			checks[1] += 1
			rcount += 1
		mainlist += 1

	while lcount < len(left):
		l[mainlist] = left[lcount]
		#swap increment
		checks[1] += 1
		lcount += 1
		mainlist += 1

	while rcount < len(right):
		l[mainlist] = right[rcount]
		#swap increment
		checks[1] += 1
		rcount += 1
		mainlist += 1
	return checks

	#print l
		

if __name__ == "__main__":
	A = listmaker()
	A2 = []
	for i in range(len(A)):
		A2.append(A[i])
	print A
	print A2
	C = mergesort(A, [0,0])
	A2.sort()
	if A == A2:
		print "OK"
	print C