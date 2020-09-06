from io import open
import random
from heuristic_functions import *

if len(sys.argv)==2:
	file = sys.argv[1]
else:
	print("\nPlease, compute on the args the '*.txt' file that contains the instance to solve")
	sys.exit()

items,n,w = read_instance(file)

# Just printing the data we have
'''
print("\n\nITEMS\n")
for i in range(0,n):
	print(str(items[i][0])+" - "+str(items[i][1]))
print('\nKnapsack capacity (w): '+str(w))
print('\nNumber of items: (n): '+str(n))
'''
menu(w,n,items)