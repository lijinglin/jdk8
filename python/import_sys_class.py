from collections import OrderedDict

langs = OrderedDict();
langs['ljl'] = 'python'
langs['daibin'] = 'c'
langs['langlin'] = 'c++'
langs['humin'] = 'go'
langs['tyq'] = 'java'

for name,lang in langs.items() :
	print name.title() + "' favorite language is " + lang;
	
	
from random import randint
for i in range(1,100):
	x=randint(1,6)
	print x	
	
	
class Die(object):
		def __init__(self,times=6):
			self.times=times
			print "Die instance created with max " + str(times)
		def rollDie(self):
			times = randint(1,self.times)
			print "Die with current side:" + str(times )

d = Die();
for i in xrange(1,30)		:
	d.rollDie()
	
d = Die(20);
for i in xrange(1,30)		:
	d.rollDie()	
	
d = Die(30);
for i in xrange(1,30)		:
	d.rollDie()	