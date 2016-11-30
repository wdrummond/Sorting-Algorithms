from Bubblesort import *
from Shakersort import *
from Selectionsort import *
import Listmaker
from Mergesort import *
from Quicksort import * 
from Modquicksort import *
from Hashsort import *
import random
import sys
import math

def main():
	sys.setrecursionlimit(5000)
	sortingFunctions = [bubblesort, shakersort, selectionsort, mergesort, quicksort, modquicksort, hashsort]
	functionNames = ["Bubblesort", "Shakersort", "Selectionsort", "Mergesort", "Quicksort", "Modquicksort", "Hashsort"]
	for i in range(len(sortingFunctions)):
		A = Listmaker.listmaker()
		A2 = A[:]
		A2.sort()
		if sortingFunctions[i] == quicksort:
			print functionNames[i] 
			C = sortingFunctions[i](A, 0, len(A)-1, [0,0] )
		elif sortingFunctions[i] == modquicksort:
			print functionNames[i]
			C = sortingFunctions[i](A, 0, len(A)-1, [0,0])
		else:
			print functionNames[i]
			C = sortingFunctions[i](A, [0,0])
		# if A != A2:
		# 	print "This is wrong."
		# else:
		# 	print "OK"

		print math.log(C[0], 2)
		#print math.log(C[1], 2)

main()