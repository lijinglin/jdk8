#coding=utf-8
import json;
def write_json(jsobj,fname) :
	try:
		with open(fname,'w') as file:
			json.dump(jsobj,file)
	except IOError:
		print "fail to write to file :" + fname;
	




		
		
def _byteify(data, ignore_dicts = False):
	# if this is a unicode string, return its string representation
	if isinstance(data, unicode):
		return data.encode('utf-8')
	# if this is a list of values, return list of byteified values
	if isinstance(data, list):
		return [ _byteify(item, ignore_dicts=False) for item in data ]
	# if this is a dictionary, return dictionary of byteified keys and values
	# but only if we haven't already byteified it
	if isinstance(data, dict) and not ignore_dicts:
		return {
			_byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=False)
			for key, value in data.iteritems()}
	else:
		return data

def read_json(fname):
	with open(fname,'r') as file:
		data = json.load(file)
		print "read json  data:" + str(data)
		return _byteify(data,False)
		

		
		

mydict={'name':'ljl','age':42, 'gender':'male','address':{'city':'shenzhen','zipcode':'580055'}}

filename='d:/a.json'
write_json(mydict,filename)
dict1 = read_json(filename)
print "dict is " + str(dict1)

print dict1["name"] + " " + str(dict1["age"])