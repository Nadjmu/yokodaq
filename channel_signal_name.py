# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'channel_signal_name.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np 

class Ui_signalNames(object):
    selected_channel = np.array([])
    ch = np.zeros((6,30),dtype=bool)
    signal_names = []
    def __init__(self,selected_channel):
        self.selected_channel = selected_channel.astype(int)
        #print(self.selected_channel)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 600)
        MainWindow.setStyleSheet("background: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.topLabels()
        self.labels()
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def topLabels(self):
        self.su1 = QtWidgets.QLabel(self.centralwidget)
        self.su1.setGeometry(QtCore.QRect(55, 20, 50, 20))
        self.su1.setStyleSheet("background-color: rgb(0, 0, 127);color:rgb(255,255,255)")
        self.su1.setObjectName("su1")
        
        self.su2 = QtWidgets.QLabel(self.centralwidget)
        self.su2.setGeometry(QtCore.QRect(215, 20, 50, 20))
        self.su2.setStyleSheet("background-color: rgb(0, 0, 127);color:rgb(255,255,255)")
        self.su2.setObjectName("su2")
        
        self.su3 = QtWidgets.QLabel(self.centralwidget)
        self.su3.setGeometry(QtCore.QRect(375, 20, 50, 20))
        self.su3.setStyleSheet("background-color: rgb(0, 0, 127);color:rgb(255,255,255)\n")
        self.su3.setObjectName("su3")
        
        self.su4 = QtWidgets.QLabel(self.centralwidget)
        self.su4.setGeometry(QtCore.QRect(535, 20, 50, 20))
        self.su4.setStyleSheet("background-color: rgb(0, 0, 127);color:rgb(255,255,255)")
        self.su4.setObjectName("su4")
        
        self.su5 = QtWidgets.QLabel(self.centralwidget)
        self.su5.setGeometry(QtCore.QRect(695, 20, 50, 20))
        self.su5.setStyleSheet("background-color: rgb(0, 0, 127);color:rgb(255,255,255)")
        self.su5.setObjectName("su5")
        
        self.su6 = QtWidgets.QLabel(self.centralwidget)
        self.su6.setGeometry(QtCore.QRect(855, 20, 50, 20))
        self.su6.setStyleSheet("background-color: rgb(0, 0, 127);color:rgb(255,255,255)")
        self.su6.setObjectName("su6")
        
        self.ch_lab_1 = QtWidgets.QLabel(self.centralwidget)
        self.ch_lab_1.setGeometry(QtCore.QRect(20, 50, 49, 20))
        self.ch_lab_1.setStyleSheet("background-color: rgb(0, 0, 127);color:rgb(255,255,255)")
        self.ch_lab_1.setObjectName("ch_lab_1")
        self.sig_lab_1 = QtWidgets.QLabel(self.centralwidget)
        self.sig_lab_1.setGeometry(QtCore.QRect(70, 50, 70, 20))
        self.sig_lab_1.setStyleSheet("background-color: rgb(0, 0, 127);color:rgb(255,255,255)")
        self.sig_lab_1.setObjectName("sig_lab_1")
        self.sig_lab_2 = QtWidgets.QLabel(self.centralwidget)
        self.sig_lab_2.setGeometry(QtCore.QRect(230, 50, 70, 20))
        self.sig_lab_2.setStyleSheet("background-color: rgb(0, 0, 127);color:rgb(255,255,255)")
        self.sig_lab_2.setObjectName("sig_lab_2")
        self.ch_lab_2 = QtWidgets.QLabel(self.centralwidget)
        self.ch_lab_2.setGeometry(QtCore.QRect(180, 50, 49, 20))
        self.ch_lab_2.setStyleSheet("background-color: rgb(0, 0, 127);color:rgb(255,255,255)")
        self.ch_lab_2.setObjectName("ch_lab_2")
        self.sig_lab_3 = QtWidgets.QLabel(self.centralwidget)
        self.sig_lab_3.setGeometry(QtCore.QRect(390, 50, 70, 20))
        self.sig_lab_3.setStyleSheet("background-color: rgb(0, 0, 127);color:rgb(255,255,255)")
        self.sig_lab_3.setObjectName("sig_lab_3")
        self.ch_lab_3 = QtWidgets.QLabel(self.centralwidget)
        self.ch_lab_3.setGeometry(QtCore.QRect(340, 50, 49, 20))
        self.ch_lab_3.setStyleSheet("background-color: rgb(0, 0, 127);color:rgb(255,255,255)")
        self.ch_lab_3.setObjectName("ch_lab_3")
        self.sig_lab_4 = QtWidgets.QLabel(self.centralwidget)
        self.sig_lab_4.setGeometry(QtCore.QRect(550, 50, 70, 20))
        self.sig_lab_4.setStyleSheet("background-color: rgb(0, 0, 127);color:rgb(255,255,255)")
        self.sig_lab_4.setObjectName("sig_lab_4")
        self.ch_lab_4 = QtWidgets.QLabel(self.centralwidget)
        self.ch_lab_4.setGeometry(QtCore.QRect(500, 50, 49, 20))
        self.ch_lab_4.setStyleSheet("background-color: rgb(0, 0, 127);color:rgb(255,255,255)")
        self.ch_lab_4.setObjectName("ch_lab_4")
        self.sig_lab_5 = QtWidgets.QLabel(self.centralwidget)
        self.sig_lab_5.setGeometry(QtCore.QRect(710, 50, 70, 20))
        self.sig_lab_5.setStyleSheet("background-color: rgb(0, 0, 127);color:rgb(255,255,255)")
        self.sig_lab_5.setObjectName("sig_lab_5")
        self.ch_lab_5 = QtWidgets.QLabel(self.centralwidget)
        self.ch_lab_5.setGeometry(QtCore.QRect(660, 50, 49, 20))
        self.ch_lab_5.setStyleSheet("background-color: rgb(0, 0, 127);color:rgb(255,255,255)")
        self.ch_lab_5.setObjectName("ch_lab_5")
        self.sig_lab_6 = QtWidgets.QLabel(self.centralwidget)
        self.sig_lab_6.setGeometry(QtCore.QRect(870, 50, 70, 20))
        self.sig_lab_6.setStyleSheet("background-color: rgb(0, 0, 127);color:rgb(255,255,255)")
        self.sig_lab_6.setObjectName("sig_lab_6")
        self.ch_lab_6 = QtWidgets.QLabel(self.centralwidget)
        self.ch_lab_6.setGeometry(QtCore.QRect(820, 50, 49, 20))
        self.ch_lab_6.setStyleSheet("background-color: rgb(0, 0, 127);color:rgb(255,255,255)")
        self.ch_lab_6.setObjectName("ch_lab_6")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 70, 100, 500))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(200, 70, 100, 500))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(360, 70, 100, 500))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(520, 70, 100, 500))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(680, 70, 100, 500))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(840, 70, 100, 500))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(970, 520, 30, 30))
        self.save.setIcon(QtGui.QIcon('png/save.png'))
        self.save.setIconSize(QtCore.QSize(25,25))
        self.save.setObjectName("save")
        self.save.clicked.connect(self.createSignalNamesList)
        
        self.gridLayout.setVerticalSpacing(2)
        #self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(2)
        self.gridLayout_3.setVerticalSpacing(2)
        self.gridLayout_4.setVerticalSpacing(2)
        self.gridLayout_5.setVerticalSpacing(2)
        self.gridLayout_6.setVerticalSpacing(2)
    
    
    def createSignalNamesList(self):
        self.signal_names=[]
        for i in np.arange(6):
            for k in np.arange(30):
                if self.ch[i][k]==True:
                    if i==0:
                        item = self.gridLayout.itemAt(3*k+2).widget()
                        self.signal_names.append(item.text())
                    if i==1:
                        item = self.gridLayout_2.itemAt(3*k+2).widget()
                        self.signal_names.append(item.text())
                    if i==2:
                        item = self.gridLayout_3.itemAt(3*k+2).widget()
                        self.signal_names.append(item.text())
                    if i==3:
                        item = self.gridLayout_4.itemAt(3*k+2).widget()
                        self.signal_names.append(item.text())
                    if i==4:
                        item = self.gridLayout_5.itemAt(3*k+2).widget()
                        self.signal_names.append(item.text())
                    if i==5:
                        item = self.gridLayout_6.itemAt(3*k+2).widget()
                        self.signal_names.append(item.text())
        #print(self.signal_names)
    
    def decodeSelectedChannel(self):
        for i in self.selected_channel:
            subunit = int(i/100)
            channel = i%100
            self.ch[subunit][channel-1] = True
    
    def setToFalse(self):
        for i in np.arange(6):
            for k in np.arange(30):
                if self.ch[i][k]==True:
                    self.ch[i][k]=False
        
    def labels(self):
        self.setToFalse()
        self.decodeSelectedChannel()
        colSize = 3
        
        #0
        count = 0
        
        for i in np.arange(30):
            lab1 = QtWidgets.QLabel(self.gridLayoutWidget)
            lab1.setAlignment(QtCore.Qt.AlignCenter)
            lab2 = QtWidgets.QLabel(self.gridLayoutWidget)
            
            lab3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
            lab3.setAlignment(QtCore.Qt.AlignCenter)
            
            lab2.setText("  ")
            
            if self.ch[0][i]==True:
                lab1.setText(str(i+1))
                lab3.setText("--")
            else: 
                lab1.setText("    ")
                lab3.hide()
            
            self.gridLayout.addWidget(lab1,int(count/colSize), count%colSize,1,1)
            self.gridLayout.addWidget(lab2,int(count/colSize), count%colSize+1,1,1)
            self.gridLayout.addWidget(lab3,int(count/colSize), count%colSize+2,1,1)
            
            count += 3
        
        #1
        count = 0
        
        for i in np.arange(30):
            lab1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
            lab1.setAlignment(QtCore.Qt.AlignCenter)
            lab2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
            
            lab3 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
            lab3.setAlignment(QtCore.Qt.AlignCenter)
            
            lab2.setText("  ")
            
            if self.ch[1][i]==True:
                lab1.setText(str(i+1))
                lab3.setText("--")
            else: 
                lab1.setText("    ")
                lab3.hide()
            
            self.gridLayout_2.addWidget(lab1,int(count/colSize), count%colSize,1,1)
            self.gridLayout_2.addWidget(lab2,int(count/colSize), count%colSize+1,1,1)
            self.gridLayout_2.addWidget(lab3,int(count/colSize), count%colSize+2,1,1)
            
            count += 3
        
        #2
        count = 0
        
        for i in np.arange(30):
            lab1 = QtWidgets.QLabel(self.gridLayoutWidget_3)
            lab1.setAlignment(QtCore.Qt.AlignCenter)
            lab2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
            
            lab3 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
            lab3.setAlignment(QtCore.Qt.AlignCenter)
            
            lab2.setText("  ")
            
            if self.ch[2][i]==True:
                lab1.setText(str(i+1))
                lab3.setText("--")
            else: 
                lab1.setText("    ")
                lab3.hide()
            
            self.gridLayout_3.addWidget(lab1,int(count/colSize), count%colSize,1,1)
            self.gridLayout_3.addWidget(lab2,int(count/colSize), count%colSize+1,1,1)
            self.gridLayout_3.addWidget(lab3,int(count/colSize), count%colSize+2,1,1)
            
            count += 3
        
        #3
        count = 0
        
        for i in np.arange(30):
            lab1 = QtWidgets.QLabel(self.gridLayoutWidget_4)
            lab1.setAlignment(QtCore.Qt.AlignCenter)
            lab2 = QtWidgets.QLabel(self.gridLayoutWidget_4)
            
            lab3 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
            lab3.setAlignment(QtCore.Qt.AlignCenter)
            
            lab2.setText("  ")
            
            if self.ch[3][i]==True:
                lab1.setText(str(i+1))
                lab3.setText("--")
            else: 
                lab1.setText("    ")
                lab3.hide()
            
            self.gridLayout_4.addWidget(lab1,int(count/colSize), count%colSize,1,1)
            self.gridLayout_4.addWidget(lab2,int(count/colSize), count%colSize+1,1,1)
            self.gridLayout_4.addWidget(lab3,int(count/colSize), count%colSize+2,1,1)
            
            count += 3
            
        #4
        count = 0
        
        for i in np.arange(30):
            lab1 = QtWidgets.QLabel(self.gridLayoutWidget_5)
            lab1.setAlignment(QtCore.Qt.AlignCenter)
            lab2 = QtWidgets.QLabel(self.gridLayoutWidget_5)
            
            lab3 = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
            lab3.setAlignment(QtCore.Qt.AlignCenter)
            
            lab2.setText("  ")
            
            if self.ch[4][i]==True:
                lab1.setText(str(i+1))
                lab3.setText("--")
            else: 
                lab1.setText("    ")
                lab3.hide()
            
            self.gridLayout_5.addWidget(lab1,int(count/colSize), count%colSize,1,1)
            self.gridLayout_5.addWidget(lab2,int(count/colSize), count%colSize+1,1,1)
            self.gridLayout_5.addWidget(lab3,int(count/colSize), count%colSize+2,1,1)
            
            count += 3
            
        #5
        count = 0
        
        for i in np.arange(30):
            lab1 = QtWidgets.QLabel(self.gridLayoutWidget_6)
            lab1.setAlignment(QtCore.Qt.AlignCenter)
            lab2 = QtWidgets.QLabel(self.gridLayoutWidget_6)
            
            lab3 = QtWidgets.QLineEdit(self.gridLayoutWidget_6)
            lab3.setAlignment(QtCore.Qt.AlignCenter)
            
            lab2.setText("  ")
            
            if self.ch[5][i]==True:
                lab1.setText(str(i+1))
                lab3.setText("--")
            else: 
                lab1.setText("    ")
                lab3.hide()
            
            self.gridLayout_6.addWidget(lab1,int(count/colSize), count%colSize,1,1)
            self.gridLayout_6.addWidget(lab2,int(count/colSize), count%colSize+1,1,1)
            self.gridLayout_6.addWidget(lab3,int(count/colSize), count%colSize+2,1,1)
            
            count += 3
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.su1.setText(_translate("MainWindow", " Subunit 0"))
        self.su2.setText(_translate("MainWindow", " Subunit 1"))
        self.su3.setText(_translate("MainWindow", " Subunit 2"))
        self.su4.setText(_translate("MainWindow", " Subunit 3"))
        self.su5.setText(_translate("MainWindow", " Subunit 4"))
        self.su6.setText(_translate("MainWindow", " Subunit 5"))
        self.ch_lab_1.setText(_translate("MainWindow", " Channel"))
        self.sig_lab_1.setText(_translate("MainWindow", " Signal Name"))
        self.sig_lab_2.setText(_translate("MainWindow", " Signal Name"))
        self.ch_lab_2.setText(_translate("MainWindow", " Channel"))
        self.sig_lab_3.setText(_translate("MainWindow", " Signal Name"))
        self.ch_lab_3.setText(_translate("MainWindow", " Channel"))
        self.sig_lab_4.setText(_translate("MainWindow", " Signal Name"))
        self.ch_lab_4.setText(_translate("MainWindow", " Channel"))
        self.sig_lab_5.setText(_translate("MainWindow", " Signal Name"))
        self.ch_lab_5.setText(_translate("MainWindow", " Channel"))
        self.sig_lab_6.setText(_translate("MainWindow", " Signal Name"))
        self.ch_lab_6.setText(_translate("MainWindow", " Channel"))
        #self.save.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_signalNames()
    ui.setupUi(MainWindow,np.arange(180))
    MainWindow.show()
    sys.exit(app.exec_())

