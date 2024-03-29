import socket
import threading
import time

#连接服务器
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverAddress = ('ryanxin.cn', 11111)

s.connect(serverAddress)
myAddress = s.getsockname() #本机ip端口
chain = input('连接口令：')
send = ('#connectChain*'+chain).encode()
s.sendall(send)
myPeer = eval(s.recv(2048).decode())  # peer ip端口
print('myAddress: ', myAddress)
print('got myPeer: ', myPeer)
s.close()

#发送一个TCP连接，用于打洞，无需对方接收
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(myAddress)
try:
    s.connect(myPeer)
except ConnectionRefusedError:
    print('已尝试打洞')
s.close()

#监听TCP连接
sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sc.bind(myAddress)
sc.listen(1)
s, address = sc.accept()
sc.close()

#聊天
def sendToMyPeer():
    while True:
        send_text = input("我方发送：")
        s.sendall(send_text.encode())


def recFromMyPeer():
    while True:
        message = s.recv(2048).decode()
        print('\r对方回复：'+message+'\n我方发送：', end='')

sen_thread = threading.Thread(target=sendToMyPeer)
rec_thread = threading.Thread(target=recFromMyPeer)

rec_thread.start()
sen_thread.start()


sen_thread.join()
rec_thread.join()
