import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


class Windows(QtWidgets.QWidget):
   def __init__(self):
      super(Windows, self).__init__()
      self.initUI()

   def initUI(self, ):
      # 设置窗口参数
      self.resize(600, 360)  # 设置窗口大小
      self.setWindowTitle("第一个PyQt桌面应用")  # 设置窗口标题
      self.setFixedSize(self.width(), self.height())  # 禁用最大化

      # 添加一个按钮
      self.btn = QPushButton("弹出消息框", self)
      self.btn.setFont(QFont('黑体', 9, QFont.Bold))
      self.btn.resize(120, 80)
      self.btn.move(self.width() / 2 - 60, self.height() / 2 - 40)
      self.btn.clicked.connect(self.Message)  # 弹出消息框

      self.show()

   def Message(self):
      self.mBox = QMessageBox.information(self, "欢迎提示", "欢迎来到编码魔坊！")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = Windows()
    sys.exit(app.exec_())
