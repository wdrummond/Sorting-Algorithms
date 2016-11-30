import random

#A = [21, 13, 48, 66, 12, 50, 92, 1]

def listmaker():
	alist = []
	for i in range(21):
		num = random.randrange(100)
		alist.append(num)
	return alist


def bubblesort(l, checks):
	sort = True
	while sort == True:
		sort = False
		for i in range(len(l)-1):
			#compare increment
			checks[0] += 1
			if l[i] > l[i+1]:
				#print l[i]
				holder = l[i]
				l[i] = l[i+1]
				l[i+1] = holder
				#swap increment
				checks[1] += 1
				sort = True
			else:
				pass
	return checks
	#print l

if __name__ == "__main__":
	A = listmaker()
	A2 = []
	for i in range(len(A)):
		A2.append(A[i])
	print A
	print A2
	C = bubblesort(A, [0,0])
	A2.sort()
	if A == A2:
		print "OK"
	print C