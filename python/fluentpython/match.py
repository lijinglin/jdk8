import sys
import re

wordRe = re.compile(r'\w+')
index = {}

with open('d:\\ITER.TXT',encoding='utf-8') as fp:
	for line_no,line in enumerate(fp,1):
		for match in wordRe.finditer(line):
			word = match.group()
			print( word)
			column_no = match.start() + 1
			location = (line_no,column_no)
			occurences = index.get(word,[])
			occurences.append(location)
			index[word] = occurences ;

for word in sorted(index,key=str.upper):
	print(word,index[word])