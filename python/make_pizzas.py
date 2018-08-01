import pizza_module as pizza
pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12,'mushrooms','green peppers', 'extra cheese')


from pizza_module import make_pizza
make_pizza(20,'pepperoni')
make_pizza(30,'mushrooms','green peppers', 'extra cheese')

from pizza_module import make_pizza as make
make(25,'pepperoni')
make(35,'mushrooms','green peppers', 'extra cheese')


from pizza_module import *
make_pizza(25,'pepperoni')
make_pizza(35,'mushrooms','green peppers', 'extra cheese')
