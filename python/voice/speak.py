#coding=utf-8
import sys
 
reload(sys)
sys.setdefaultencoding('utf8')
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("了解了")

