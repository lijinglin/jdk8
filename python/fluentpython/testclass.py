#coding=utf-8
class p:
    """ this is a basic class """
    basicInfo={"name":"lxh","nation":"China"}; # 类成员变量
    def __init__(self): # 类成员函数需要传入self关键字
		""" this is a init function of basic class """
		print "this is a init function ... ";
		print p.basicInfo
    def sub(self,a,b): # 类成员函数需要传入self关键字
        """ this is a common function of basic class """
        return a-b;
# 类实例化
a=p();
# 调用类方法
print a.sub(40,5); # -1