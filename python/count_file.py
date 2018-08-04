def count_file(fileName):
	try:
		with open(fileName) as file:
			content = file.read();
	except IOError:
		print 'sorry ,can not file the file for:' + fileName;
	else:
		print "total word counts" + str(len(content.split()))
		
count_file('d:/alice.txt')		
count_file('d:/mobydick.txt')		