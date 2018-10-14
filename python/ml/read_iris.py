import os
import pandas as pd	

def get_data():
	PATH="d:\\"
	file_name = PATH+'iris.data'	
	os.chdir(PATH)
	df = pd.read_csv(file_name,	names=['sepal length','sepal width','petal length','petal width','class'])
	return df