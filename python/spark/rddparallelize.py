rdd1 = sc.parallelize([(1,2),(3,4),(3,6),(2,5),(4,6),(1,9)])
rdd2 = sc.parallelize([(3,9),(4,2)])
rdd_word_num = rdd1.mapValues(lambda v: (v,1));
sumcount = rdd_word_num.reduceByKey(lambda x,y: (x[0] + y[0],x[1] + y[1]))
avg = sumcount.mapValues(lambda x : float(x[0])/x[1])

def print_rdd(rdd):
    for e in rdd.take(10):
      print e
              
print_rdd(avg)

def reduceFunc(value):
    sum = 0;
    for c in value:
       sum += c
    return sum

result = rdd1.groupByKey().mapValues(reduceFunc)

print_rdd(result)