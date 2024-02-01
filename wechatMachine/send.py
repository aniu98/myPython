import time

from wxauto import *
# from MysqlDb import MysqlDb

# def sendTodaySche():
#     mysqldb = MysqlDb("schedule")
#     thisMonth = datetime.today().__format__("%Y-%m")
#     today = datetime.today().__format__("%m-%d").split('-')
    
#     result = mysqldb.sql_select("SELECT * FROM `" + thisMonth + "` WHERE date = '" + today + "'")["data"]
#     msgs = ["今日值班人员如下："]
#     for i in range(0,len(tempMsgs)):
#         if '、' in result[0][i+2]:
#             splitStrs =  result[0][i+2].split("、")
#             temp = []
#             for k in range(0,len(splitStrs)):
#                 if i == 0 and k == 1:
#                     temp.append("、"+splitStrs[k])
#                 else:
#                     temp.append("@"+splitStrs[k])
#             temp[0] = tempMsgs[i]+temp[0]
#             msgs.append(temp)
#         else:
#             msgs.append(tempMsgs[i] + '@' + result[0][i+2])
msgs="今日值班人员如下： 阿牛"
def SendWrapAndATMsg(self,msgs, clear=True):
    '''向当前窗口发送换行消息和@消息
    msgs : 要发送的消息列表
    clear : 是否清除当前已编辑内容
    '''
    self.UiaAPI.SwitchToThisWindow()
    if clear:
        self.EditMsg.SendKeys('{Ctrl}a', waitTime=0)
    for i in range(0,len(msgs)):
        if type(msgs[i]) ==type([]):
            for k in range(0,len(msgs[i])):
                self.EditMsg.SendKeys(msgs[i][k], waitTime=0)
                if i == 1 and k == 1:
                    pass
                else:
                    self.EditMsg.SendKeys('{Enter}', waitTime=0)
            self.EditMsg.SendKeys('{Shift}{Enter}', waitTime=0)
        else:
            self.EditMsg.SendKeys(msgs[i], waitTime=0)
            if i > 1:
                self.EditMsg.SendKeys('{Enter}', waitTime=0)
            self.EditMs备g.SendKeys('{Shift}{Enter}', waitTime=0)
    self.EditMsg.SendKeys('{Enter}', waitTime=0)

wechat = WeChat()
wechat.ChatWith("东逝水")
# wechat.SendMsg(msg=msgs)
msgGet= wechat.GetLastMessage
print(msgGet)
wechat.SendMsg(msg=msgGet[1])

def listening(who = '东东'):
    wechat = WeChat()
    wechat.ChatWith(who)
    lastMsg = []
    while True: 
        newMsg = wechat.GetLastMessage
        if newMsg[0]=='东东' and lastMsg != newMsg:
            pass
        time.sleep(1)
        