import sys
from operator import itemgetter,attrgetter

items = []
item = []

def get_data(text): # Validates integer values are given
	try:
		cast = int(input(text + " > ")) # Casts to integer
	except ValueError:
		print("\nYou can type just integer values! ") # If the value inputed, isn't an integer, throws a error message
		sys.exit()
	return cast

def writes_result(file_name,objective_f,heuristic):
	file = open(file_name,'a')
	file.write("\n--------------------------------\n"
		+"Heuristic #"+str(heuristic)+"\n"
		+"k = "+str(objective_f))
	file.close()


def objective_f(w,items,n): # Evaluates the data to decide if put it or not on the backpack
	elements = set() # To store in a set the items put on the backpack
	current_w = w # The variable will be updating according to the items put
	k = 0 # Initialize k to work
	for i in range(0,n):
		# print(str(items[i][0])+" "+str(items[i][1])+" <= "+str(current_w)+str(" = ")+str(items[i][1]<=current_w))
		if(items[i][2]<=current_w): # If Wi fits on the backpack, puts item
			k += items[i][1] # Total gain updates (Objective Function)
			current_w -= items[i][2] # Current capacity of the backpack updates
			elements.add(items[i][0]) # Adds the put item on the set
		if(current_w==0): # If current capacity = 0, the following items won't fit, so stops the evualation
			break;
	#print("The objects put on the Knapsack are: "+str(elements)) # Prints the put items on the backpack
	print("\nThe Objective Function = "+str(k)+"\n\n\n") # Prints the final gain
	return k

def calculate_b(items_sort,n):
	aux_items_sort = [] # Auxiliar variable to work
	for i in range(0,n):
		bi = items_sort[i][1] / items_sort[i][2] # Makes Vi/Wi
		aux_items_sort.append([(i+1),bi,items_sort[i][1],items_sort[i][2]])
		'''Appends auxiliar variables something like this:
		[ index of item , bi , vi , wi ]
		'''
	aux_items_sort.sort(key=itemgetter(1),reverse=True) # Sorts the aux variables by highest bi
	for i in range(0,n):
		del aux_items_sort[i][1] 
		'''Once sorted, we delete the bi value, because it's already sorted by highest bi
		The objective_f needs to recive on the paramater "items" an array in this way.
		That's why we need to delate the bi values
		[ index of the item , vi, wi ]
		'''
	return aux_items_sort

def read_instance(data):
	with open(data,'r') as file: # Reading the instance and making validations
		i = 0
		for line in file:
			try:
				if((int(line.split()[0]))>0 and (int(line.split()[1]))>0): # Validates if values are positive and > 0
					item = [i,int(line.split()[0]),int(line.split()[1])]	
					items.append(item)
					'''Appends something like this to items[array]
					[[ index of the item , vi , wi ]]
					'''
					i+=1
				else:
					print("\nNo negative values allowed, please correct the values of "
						+str(data)) # Stops the program if fins negative values
					sys.exit()

			except ValueError: # Validates if values are integer
				print("\nPlease, correct the values of "+str(data)+" , characters and not "
					"integer values are not allowed")
				sys.exit()

	n = items[0][1] # Reads the number of items
	w = items[0][2] # Reads the knapsack capacity
	del items[0]
	return items,n,w 

def copy(value):
	reseted = None
	reseted = value[:]
	return reseted

def menu(w,n,items):
	while True:
		items_sort = copy(items)
		option = input("\nSelect the heuristic to solve the Knapsack Problem:"
		"\n[1] Heuristic #1 (Putting by the highest value)"
	 	"\n[2] Heuristic #2 (Putting by the lowest weight)"
	 	"\n[3] Heuristic #3 (Putting proportionally for its value and weight)" 
		"\n[4] Exit"
		"\n\n > ")
		if option == "1":
			print("\nHEURISTIC #1\n")
			items_sort.sort(key=itemgetter(1),reverse=True) # Sort [items_sort] by higher Vi
			k = objective_f(w,items_sort,n) # Send the data to start the evaluation and gets Objective Function
		
		elif option == "2":
			print("\nHEURISTIC #2\n")
			items_sort.sort(key=itemgetter(2)) # Sort [items_sort] by higher Wi
			k = objective_f(w,items_sort,n) # Send the data to start the evaluation and gets Objective Function

		elif option == "3":
			print("\nHEURISTIC #3\n")
			items_sort = calculate_b(items_sort,n) # Returns [items_sort] a sorted array by higher bi
			k = objective_f(w,items_sort,n) # Send the data to start the evaluation and gets Objective Function

		elif option == "4":
			print("Goodbye!")
			break;
		else:
			print("Invalid option")
