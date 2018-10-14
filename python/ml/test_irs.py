import read_iris
dfd = read_iris.get_data()
print dfd.head()
print(type(dfd))
df = dfd
print dfd.loc[dfd.index[[0, 2]], 'sepal length']

print dfd.loc[dfd.index[[0, 2,4]],[x for x in dfd.columns if 'width' in x]]

print dfd.iloc[[0,3,4],dfd.columns.get_indexer(['sepal length']) ]
