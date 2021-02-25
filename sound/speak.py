# pip install pyttsx3
import pyttsx3


engine = pyttsx3.init()
engine.say('你好啊.')
engine.say('我要开始休息5分钟了')
engine.runAndWait()

voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   print(voice.id)
   engine.say('我的休息结束了 ')
engine.runAndWait()