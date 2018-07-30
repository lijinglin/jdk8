def make_shirt(size='XL',title='I Love Python'):
	print "Shirt with size:" + size + " title is:" +title.title()


make_shirt("M")
make_shirt(title='hello jeans')
make_shirt()


def make_pizza(size,*toppings):
	print("\n making a " + str(size) + "-inch pizza with following toppings")
	for topping in toppings :
		print("-" + topping)

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers', 'extra cheese')