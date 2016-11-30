import random

def listmaker():
	alist = []
	for i in range(2048):
		num = random.randrange(2048)
		alist.append(num)
	return alist