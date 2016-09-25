grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
print (grocery_list)
print ("First Item", grocery_list[0])

grocery_list[0] = "Green Juice"
print("grocery_list[0]: ", grocery_list[0])
print("grocery_list[1:3]: ", grocery_list[1:3])

other_events = ['Wash Car', 'Pick Up Kids', 'Cash Check']
to_do_list = [other_events, grocery_list]
print ("to_do_list: ", to_do_list)
print ("to_do_list[1][1]: ", to_do_list[1][1])


print ("\n"*2)

print ("original: ", grocery_list)

grocery_list.append("Onions")
print ("append Onions: ", grocery_list)

grocery_list.insert(1, "Pickle")
print ("insert Pickle in index-1: ", grocery_list)

grocery_list.remove("Potatoes")
print ("remove Potatoes: ", grocery_list)

grocery_list.pop(1)
print ("pop 1: ", grocery_list)

grocery_list.sort()
print ("sort: ", grocery_list)

grocery_list.reverse()
print ("reverse: ", grocery_list)