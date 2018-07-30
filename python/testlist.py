list = ['a','b','c','a','dd','e','a']
def clearList(alist):
  list = alist[:]
  print('len:'+ str(len(alist)))
  end = len(list)
  for index in range(0,end):
    print index
    reverseIndex = end -index - 1;
    if(list[reverseIndex] == 'a'):
        print(reverseIndex)
        print list.pop(reverseIndex)
        
clearList(list)