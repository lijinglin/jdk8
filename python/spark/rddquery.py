class SearchFunctions(object):
  def __init__(self,query):
    self.query = query
  def isMatch(self,s ):
    return self.query in s
  def getMatchesFunctionReference(self,rdd):
    return rdd.filter(self.isMatch)
  def getMatchesMemberReference(self,rdd):
    query = self.query
    return rdd.filter(lambda x: query in x)

	
'''


lines = sc.textFile("d:/iris.data")
s =SearchFunctions('vir')
vlines = s.getMatchesMemberReference(lines)
print vlines.count()
for line in vlines.take(10):
  print(line)

 
 #use map  reduce to count average:
 
 r4 =sc.parallelize(range(0,100000))
 count,sum =r4.map(lambda i : (1,i)).reduce(lambda x,y: (x[0] + y[0],x[1]+y[1]))
 average = float(fum)/count
 
 #other aggregate
  sumcount = r4.aggregate((0,0),(lambda acc,value:(acc[0]+value,acc[1] +1)), (lambda acc1,acc2:(acc1[0]+acc2[0],acc1[1]+acc2[1])))
  '''