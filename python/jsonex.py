#coding=iso8859
import json;
def write_json(jsobj,fname) :
	try:
		with open(fname,'w') as file:
			json.dump(jsobj,file)
	except IOError:
		print "fail to write to file :" + fname;
	



def read_json(fname):
    with open(fname,'r') as file:
        return json.load(file)
		

mydict={'name':'ljl','age':42, 'gender':'male'}
filename='d:/a.json'
write_json(mydict,filename)
other = read_json(filename)
print other
#print other["name"] + " " + other["age"]