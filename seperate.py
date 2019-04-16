from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton,QFileDialog, QShortcut
from PyQt5.QtCore import QRect
from PyQt5.Qt import QLineEdit
import sys
import os
import shutil
import numpy as np
import matplotlib.pyplot as plt
import pyqtgraph as pg

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "window"
        self.top = 200
        self.left = 200
        self.width = 1000
        self.height =800
        self.CreatInteraction()
        self.InitWindow()
        self.num = 0
        self.files_name = []
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()

    def CreatInteraction(self):
        #按键
        self.button_load = QPushButton("加载", self)
        self.button_load.setGeometry(QRect(0, 0, 80, 25))
        self.button_load.clicked.connect(self.LoadFile)

        self.button_load = QPushButton("h", self)
        self.button_load.setGeometry(QRect(100, 0, 60, 25))
        self.button_load.clicked.connect(self.Fileh)
        self.button_load = QPushButton("j", self)
        self.button_load.setGeometry(QRect(100, 30, 60, 25))
        self.button_load.clicked.connect(self.Filej)
        self.button_load = QPushButton("k", self)
        self.button_load.setGeometry(QRect(100, 60, 60, 25))
        self.button_load.clicked.connect(self.Filek)
        self.button_load = QPushButton("l", self)
        self.button_load.setGeometry(QRect(100, 90, 60, 25))
        self.button_load.clicked.connect(self.Filel)

        self.button_load = QPushButton("跳转", self)
        self.button_load.setGeometry(QRect(800, 100, 60, 25))
        self.button_load.clicked.connect(self.jump)

        self.press_h = QShortcut("h", self)
        self.press_j = QShortcut("j", self)
        self.press_k = QShortcut("k", self)
        self.press_l = QShortcut("l", self)
        self.press_h.activated.connect(self.hPart)
        self.press_j.activated.connect(self.jPart)
        self.press_k.activated.connect(self.kPart)
        self.press_l.activated.connect(self.lPart)

        self.textbox_h = QLineEdit(self)
        self.textbox_h.move(180, 0)
        self.textbox_h.resize(400, 25)
        self.num_h = QLineEdit(self)
        self.num_h.move(600, 0)
        self.num_h.resize(80, 25)

        self.textbox_j = QLineEdit(self)
        self.textbox_j.move(180, 30)
        self.textbox_j.resize(400, 25)
        self.num_j = QLineEdit(self)
        self.num_j.move(600, 30)
        self.num_j.resize(80, 25)

        self.textbox_k = QLineEdit(self)
        self.textbox_k.move(180, 60)
        self.textbox_k.resize(400, 25)
        self.num_k = QLineEdit(self)
        self.num_k.move(600, 60)
        self.num_k.resize(80, 25)

        self.textbox_l = QLineEdit(self)
        self.textbox_l.move(180, 90)
        self.textbox_l.resize(400, 25)
        self.num_l = QLineEdit(self)
        self.num_l.move(600, 90)
        self.num_l.resize(80, 25)

        self.textbox_msg = QLineEdit(self)
        self.textbox_msg.move(100,120)
        self.textbox_msg.resize(500,100)
        self.textbox_total = QLineEdit(self)
        self.textbox_total.setGeometry(QRect(700, 50, 80, 25))
        self.textbox_now = QLineEdit(self)
        self.textbox_now.setGeometry(QRect(700, 100, 80, 25))

        self.to_ward = QShortcut("d", self)
        self.back_ward = QShortcut("a", self)
        self.to_ward.activated.connect(self.Toward)
        self.back_ward.activated.connect(self.Backward)
 #        self.shortcut = QShortcut("u", self.Delete)
        self.plt = pg.PlotWidget(self)
        self.plt.move(30,280)
        self.plt.resize(800,400)

    def LoadFile(self):#载入文件
        self.directory = QFileDialog.getExistingDirectory(self,"选取文件夹", "./")  # 起始路径
        self.root = os.path.abspath(os.path.join(self.directory, ".."))
        for file in os.listdir(self.directory):
            self.files_name.append(os.path.join(self.directory,file))
        self.len = len(self.files_name)
        self.file_name = os.path.join(self.directory, self.files_name[self.num])
        if os.path.exists(self.file_name):
            self.pltshow(self.file_name)
        self.textbox_total.setText(str(self.len))

    def Fileh(self):
        self.dir_h = QFileDialog.getExistingDirectory(self,"选取文件夹", self.root)
        self.textbox_h.setText(str(self.dir_h))
    def Filej(self):
        self.dir_j = QFileDialog.getExistingDirectory(self,"选取文件夹", self.root)
        self.textbox_j.setText(str(self.dir_j))
    def Filek(self):
        self.dir_k = QFileDialog.getExistingDirectory(self,"选取文件夹", self.root)
        self.textbox_k.setText(str(self.dir_k))
    def Filel(self):
        self.dir_l = QFileDialog.getExistingDirectory(self,"选取文件夹", self.root)
        self.textbox_l.setText(str(self.dir_l))
    def Toward(self):
        self.num += 1
        if self.num > self.len:
            self.num = self.len
        self.file_name = os.path.join(self.directory, self.files_name[self.num])
        if os.path.exists(self.file_name):
            self.pltshow(self.file_name)
    def Backward(self):
        self.num -= 1
        if self.num<0:
            self.num = 0
        self.file_name = os.path.join(self.directory, self.files_name[self.num])
        if os.path.exists(self.file_name):
            self.pltshow(self.file_name)

    def jump(self):
        self.num = int(self.textbox_now.text())
        if os.path.exists(self.file_name):
            self.pltshow(self.file_name)


    def hPart(self):
        if os.path.exists(self.dir_h):
            shutil.move(self.file_name, self.dir_h)
    def jPart(self):
        if os.path.exists(self.dir_j):
            shutil.move(self.file_name, self.dir_j)
    def kPart(self):
        if os.path.exists(self.dir_k):
            shutil.move(self.file_name, self.dir_k)
    def lPart(self):
        if os.path.exists(self.dir_l):
            shutil.move(self.file_name, self.dir_l)




    def pltshow(self,path):
#       self.
        self.plt.clear()
        sig = open(path, "rb").read()
        sig = [i for i in sig if i != 0]
        sig = np.array(sig[0: 12 * int(len(sig) / 12)])
        data = sig.reshape(int(len(sig) / 12), 12).T
        self.plt.setXRange(0,256,padding=0)
        self.plt.setYRange(0,180,padding=0)
        self.plt.plot(data[10])
        self.textbox_now.setText(str(self.num))
        try:self.num_h.setText(str(len([name for name in os.listdir(self.dir_h) if os.path.isfile(os.path.join(self.dir_h, name))])))
        except:pass
        try:self.num_j.setText(str(len([name for name in os.listdir(self.dir_j) if os.path.isfile(os.path.join(self.dir_j, name))])))
        except:pass
        try:self.num_k.setText(str(len([name for name in os.listdir(self.dir_k) if os.path.isfile(os.path.join(self.dir_k, name))])))
        except:pass
        try:self.num_l.setText(str(len([name for name in os.listdir(self.dir_l) if os.path.isfile(os.path.join(self.dir_l, name))])))
        except:pass
if __name__=="__main__":
    App = QApplication(sys.argv)
    widow = Window()
    plt.show()
    sys.exit(App.exec())
