lines = sc.textFile('c:/app/spark/readme.md')
words = lines.flatMap(lambda line : line.split(' '))
wordcount = words.map(lambda x : (x,1))
wordcount = wordcount.partitionBy(2,lambda key : hash(key))
swc = wordcount.sortByKey(ascending=True,keyfunc=(lambda w: str(w))).reduce(lambda x,y : x+y)
#swc = swc.sortByKey(ascending=True,keyfunc=(lambda w: str(w)))

def print_rdd(rdd,num=10):
    for e in rdd.take(num):
      print e
	  
	  
print_rdd(swc,100)
