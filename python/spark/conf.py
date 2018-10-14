from pyspark import SparkConf,SparkContext
myconf = SparkConf().setMaster("local").setAppName("MyApp")
sc = SparkContext(conf=myconf)
