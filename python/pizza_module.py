def make_pizza(size,*toppings):
	print("\n making a " + str(size) + "-inch pizza with following toppings")
	for topping in toppings :
		print("-" + topping)
