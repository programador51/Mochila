from io import open
import random
from operator import itemgetter,attrgetter
from heuristic_functions import *

def generate_instace(items,capacity,min_capacity,max_capacity): # Create the instance on a .txt file
	file.write(str(n)+"\t"+str(capacity)+"\n") # Writes the number of items (n) & the capacity (w)
	for i in range(0,n): # Fills the file with random numbers
		for j in range(0,2):
			if(j==0):
				value = str(random.randint(1,101)) # Generates random Vi
			else:
				value = str(random.randint(min_capacity,max_capacity)) # Generates random Wi between the parameterss
			file.write(value+str("\t")) # Writes number genereted
		file.write("\n")

print("Type the intervals for the weight") # Gets the w(min) and w(max) for the instances
w_min = get_data("\nWeight min")
w_max = get_data("\nWeight max")

if(w_min>=w_max): # Validates the intervals of weights
	print("\nIntervals are wrong! W(min) can not be >= than W(max) !")
	sys.exit()

n = get_data("\nNumber of items") # Gets the number of items for the instances (n)
m = get_data("\nNumber of instances") # Gets the number of instances to create (m)
w = int((((float(w_min)+float(w_max))/2.0)*float(n)*0.3)) # Calculates the capacity (w)
print("\nW = "+str(w))

for i in range(0,m): # Loop to solve all the instances with the data given
	items.clear() # Empties the items of the data
	print("----------------------------------------------------------------------------------")	# Esthetic
	file = open("instance"+str(i+1)+".txt",'w') # Create a file where to save information
	generate_instace(n,w,w_min,w_max) # Once created, fills it with random instance
	file.close() # Close the file, don't need it for now
	items,n,w = read_instance("instance"+str(i+1)+".txt") # Reads the file created to work with the problem
	print("\nFor instance"+str(i+1)+".txt \n") # Esthetic
	print("Items: "+str(items)) # Esthetic
	print("\nHEURISTIC #1\n")
	items_sort = copy(items) # Does a copy of the items to sort it and work with the heuristic
	items_sort.sort(key=itemgetter(1),reverse=True) # Sort [items_sort] by higher Vi
	k = objective_f(w,items_sort,n) # Send the data to start the evaluation and gets Objective Function
	writes_result("instance"+str(i+1)+".txt",k,1)
	print("\nHEURISTIC #2\n")
	items_sort.sort(key=itemgetter(2)) # Sort [items_sort] by higher Wi
	k = objective_f(w,items_sort,n) # Send the data to start the evaluation and gets Objective Function
	writes_result("instance"+str(i+1)+".txt",k,2)
	print("\nHEURISTIC #3\n")
	items_sort = calculate_b(items_sort,n) # Returns [items_sort] a sorted array by higher bi
	k = objective_f(w,items_sort,n) # Send the data to start the evaluation and gets Objective Function
	writes_result("instance"+str(i+1)+".txt",k,3)