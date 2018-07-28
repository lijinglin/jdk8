#coding=utf-8
import pyttsx
import sys
reload(sys)
sys.setdefaultencoding('utf8')
engine = pyttsx.init()
voices = engine.getProperty('voices')

for voice in voices:
 engine.say('begin say');
 engine.setProperty('voice', voice.id)
 engine.say('声音怎么样')
 engine.say('能说清楚么？')
 engine.say('end say')
engine.runAndWait()