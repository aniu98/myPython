from wxpy import *
 
bot = Bot()
tuling = Tuling(api_key='这里填机器人的api_key')
@bot.register(msg_types=TEXT)
def auto_reply_all(msg):
    tuling.do_reply(msg)
bot.join()


