
lines = sc.textFile("c:/app/spark/readme.md")
words = lines.flatMap(lambda x : x.split(" "))
r = words.countByValue()

key = 'Spark'
for k,v in r.items() :
    if(k == key) :
        print(k,v)
    
    
    
#combine by keys


def createcombiner( e):
    return (e,1 )
   

def accCombinerElement(acc,e):
    return (acc[0] + e, acc[1] + 1)

	
def accCombiners(left,right):
    return(left[0] + right[0] ,left[1] + right[1])

    
rdd = words.map(lambda x : (x,1))    
result = rdd.combineByKey(createcombiner,accCombinerElement,accCombiners)

for e in result.take(100):
    if(e[0] == key):
        print(e[0],e[1])