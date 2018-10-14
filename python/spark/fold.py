d = sc.parellelize([1,2,3,3])
 
d2 = d.fold(0,(lambda x,y : x+y))
print(d2)

d3 = d.fold(1,(lambda x,y : x*y))
print(d3)

def accFunc(acc,value):
    return (acc[0] + value, 1)
def aggreFunc(left,right):
    return (left[0] + right[0], left[1] + right[1])
	
sumcount = d.aggregate((0,0),accFunc,aggreFunc)avg= float( sumcount[0]) /sumcount[1]   
    
print avg