import random

def listmaker():
	alist = []
	for i in range(21):
		num = random.randrange(20)
		alist.append(num)
	return alist


def quicksort(l, low, high, checks):
	if low < high:
		pivot = low
		for i in range(low+1, high +1):
			#compare increment
			checks[0] += 1
			if l[i] <= l[low]:
				pivot += 1
				l[i], l[pivot] = l[pivot], l[i]
				#swap increment
				checks[1] += 1
		l[low], l[pivot] = l[pivot], l[low]
		#swap increment
		checks[1] += 1
		quicksort(l, low, pivot-1, checks)
		quicksort(l, pivot+1, high, checks)
	return checks




if __name__ == "__main__":
	A = listmaker()
	A2 = []
	for i in range(len(A)):
		A2.append(A[i])
	print A
	print A2
	C = quicksort(A, 0, len(A)-1 ,[0,0])
	A2.sort()
	print A
	if A == A2:
		print "OK"
	print C
		
