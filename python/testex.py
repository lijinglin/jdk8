import unittest
import jsonex
from  city import city

class TestJsonCAse(unittest.TestCase):
	def testParseObject(self):
		input={'name':'ljl','age':42, 'gender':'male','address':{'city':'shenzhen','zipcode':'580055'}}
		filename='d:/a.json'
		jsonex.write_json(input,filename)
		output = jsonex.read_json(filename)	
		#output['age'] = 30
		for k,v in input.items():
			self.assertEqual(v, output[k]);
			print("equals key=" + k );

	def testCity(self):
		outstr = city('sandiego','chile')
		self.assertEqual(outstr,'Sandiego Chile - population 5,000,000')
	
unittest.main()