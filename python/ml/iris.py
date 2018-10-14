import requests


r=requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
PATH="d:\\"

file_name = PATH+'iris.data'
with open(file_name,'w') as f:
    f.write(r.text)
	
import os
import pandas as pd	
PATH="d:\\"
file_name = PATH+'iris.data'	
os.chdir(PATH)
df = pd.read_csv(file_name,	names=['sepal length','sepal width','petal length','petal width','class'])
df.head()
#df.ix[:3,[x for x in df.columns if 'width' in x]]


print df.index[[0,1,2,3]]

print df.index[[0, 2]]

#df[ (df['class']=='Iris-virginica') &(df['petal width'] >2.2) ]

