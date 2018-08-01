print "======================for in file===================="
with open("c:/nsi.log") as nsifile:
	for line in nsifile:
		print line.rstrip()
		
print "======================read lines===================="		
with open("c:/nsi.log") as nsifile:
	lines = nsifile.readlines()
	for line in lines:
		print line.rstrip()		