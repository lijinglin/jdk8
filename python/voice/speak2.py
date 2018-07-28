#coding=utf-8
import sys
 
reload(sys)
sys.setdefaultencoding('utf8')

 
import pyttsx
engine = pyttsx.init()
engine.say('hello world')
engine.say('买了么')
#engine.runAndWait()
#engine.endLoop()
