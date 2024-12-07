# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'minimal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from run_measurement import run_measurement
#from run_initialise import run_initialise 
from data_processing import getAllChannel,getData,getChannelData,runMeasurement,runInitialise,runChInformation

from project_window import Ui_project
from clear_window import Ui_clear

import numpy as np 
import time
import pandas as pd
import os

class Ui_MainWindow(object):
    database_mode = False
    running = False
    project_settings = []
    user_interac = ["I am here to help you","Let's get started"]
    
    
    def openProjectWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui_pro = Ui_project()
        self.ui_pro.setupUi(self.window)
        self.window.show()
        
    def openClearWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui_cle = Ui_clear()
        self.ui_cle.setupUi(self.window)
        self.window.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(512, 280)
        MainWindow.setStyleSheet("background-color: rgb(255,255,255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.thread={}
        
        self.buttons()
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def buttons(self):
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setGeometry(QtCore.QRect(40, 40, 100, 100))
        self.play.setIcon(QtGui.QIcon('png/play.PNG'))
        self.play.setIconSize(QtCore.QSize(90,90))
        self.play.setObjectName("play")
        self.play.clicked.connect(self.changeI)
        self.play.clicked.connect(self.runAq)
        
        self.project = QtWidgets.QPushButton(self.centralwidget)
        self.project.setGeometry(QtCore.QRect(140,40,100,100))
        self.project.setIcon(QtGui.QIcon('png/project.png'))
        self.project.setIconSize(QtCore.QSize(90,90))
        self.project.setObjectName("project")
        self.project.clicked.connect(self.openProjectWindow)
        
        self.hook = QtWidgets.QPushButton(self.centralwidget)
        self.hook.setGeometry(QtCore.QRect(130, 40, 10, 10))
        self.hook.setObjectName("hook")
        self.hook.setStyleSheet("background-color: rgb(255,0,0)")
        self.hook.clicked.connect(self.setDatabase)
        
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(40, 140, 100, 100))
        self.save.setIcon(QtGui.QIcon('png/save.png'))
        self.save.setIconSize(QtCore.QSize(90,90))
        self.save.setObjectName("save")
        self.save.clicked.connect(self.saveMea)
        
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(140, 140, 100, 100))
        self.clear.setIcon(QtGui.QIcon('png/delete.png'))
        self.clear.setIconSize(QtCore.QSize(90,90))
        self.clear.setObjectName("clear")
        self.clear.clicked.connect(self.openClearWindow)
        
        self.line1_e = QtWidgets.QLineEdit(self.centralwidget)
        self.line1_e.setGeometry(QtCore.QRect(276,90,200,20))
        self.line2_e = QtWidgets.QLineEdit(self.centralwidget)
        self.line2_e.setGeometry(QtCore.QRect(276,130,200,20))
        self.line3_e = QtWidgets.QLineEdit(self.centralwidget)
        self.line3_e.setGeometry(QtCore.QRect(276,170,200,20))
        self.updateUIC("Hello")
    
    def changeI(self):
        if self.running == False:
            self.running = True
            self.updateUIC("currently running")
            self.play.setIcon(QtGui.QIcon('png/stop.PNG'))
            self.play.setIconSize(QtCore.QSize(90,90))
            #self.play.setStyleSheet("image: url(:/stop_button/square.PNG);")
        elif self.running == True:
            self.running = False
            self.updateUIC("stopped running")
            self.play.setIcon(QtGui.QIcon('png/play.PNG'))
            self.play.setIconSize(QtCore.QSize(90,90))
            #self.play.setStyleSheet("image: url(:/play_button/play.PNG);")
        
    def updateUIC(self,message):
        self.user_interac.insert(0,message)
        #print(self.user_interac)
        self.line1_e.setText(self.user_interac[0])
        self.line2_e.setText(self.user_interac[1])
        self.line3_e.setText(self.user_interac[2])
    
    def saveMea(self):
        if hasattr(self,'ui_pro')==True:
            print("here")
            self.project_settings = self.ui_pro.project_settings
            parent_dir = "Projects"
            project_name = self.project_settings[0]
            directory = project_name
            path = parent_dir+"/"+directory
            if os.path.isfile("tempp.csv"):
                self.updateUIC("Measurement was saved")
                os.replace("tempp.csv",path+"/"+project_name+".csv")
                print("Measurement was saved")
            else:
                self.updateUIC("no measurement was taken")
                print("no measurement was taken")
        else:
            print("Need a project")
            self.updateUIC("Need a project")
    
    def clearTemp(self):
        self.updateUIC("file was removed")
        os.remove("tempp.csv")
    
    def setDatabase(self):
        if (self.database_mode==False):
            self.updateUIC("now sending to INFLUX")
            self.hook.setStyleSheet("background-color: rgb(0,255,0)")
            self.database_mode = True
        else:
            self.updateUIC("not sending to INFLUX")
            self.hook.setStyleSheet("background-color: rgb(255,0,0)")
            self.database_mode = False
    
    def getProjectSettings(self):
        if hasattr(self,'ui_pro')==True:
            #print("here")
            self.project_settings = self.ui_pro.project_settings
    
    def runAq(self): 
        if self.running == True:
            self.getProjectSettings() #initialise project attributes
            self.save.setEnabled(False) 
            self.clear.setEnabled(False)
            self.project.setEnabled(False)
            self.hook.setEnabled(False)
            print("Running with these project settings:",self.project_settings)
            self.thread[1] = ThreadClass(parent=None,index=1,project_settings=self.project_settings,database_mode=self.database_mode)
            self.thread[1].start()
            
        elif self.running == False:
            self.thread[1].stop()
            self.save.setEnabled(True)
            self.clear.setEnabled(True)
            self.project.setEnabled(True)
            self.hook.setEnabled(True)
        #self.play.setEnabled(False)
    
    #################################################################################################################
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

class ThreadClass(QtCore.QThread):
    def __init__(self,parent = None,index=0,project_settings=["0","0",0,np.array([0]),[0],[0]],database_mode=False):
        super(ThreadClass, self).__init__(parent)
        
        self.is_running = True
        self.index = index #index the thread number 
        
        self.project_name = project_settings[0]
        self.ip_address = project_settings[1]
        self.frequency = project_settings[2]
        self.selected_channel = project_settings[3]
        self.signal_names = project_settings[4]
        self.database_settings = project_settings[5]
        
        self.database_mode = database_mode
        
    def readData(self): ##reads and deletes the data from tmp csv
        data = pd.read_csv("temp.csv")
        os.remove("temp.csv")
        return data
    
    
    def channelInformation(self): ##reads the data from channel_info csv
        channel_info = pd.read_csv("channel_info_python.csv")
        return channel_info
    
    def run(self):
        #print(self.selected_channel)
        ref = time.time()
        
        runChInformation(self.ip_address)
        runInitialise(self.ip_address)
        
        channel_info = self.channelInformation() 
        chinfo = getChannelData(channel_info)       #chinfo
        while(self.is_running):
            if (ref-time.time()<(1/self.frequency) and self.index ==1):
                time1 = time.time()
                runMeasurement(self.ip_address)
                data = self.readData()
                measurement = getData(data) #measurement
                # print(self.selected_channel)
                # print("BEFORE LIBRARY:  ",type(self.selected_channel))
                # self.selected_channel = self.selected_channel.tolist()
                getAllChannel(measurement,chinfo,self.selected_channel,self.signal_names,self.database_settings,self.database_mode)
                ref = ref+(1/self.frequency)
                time2 = time.time()
                print("time for 1 measurement:    ",(time2-time1)*1000)

    def stop(self):
        self.is_running = False
        print('Stopping thread...')
        #self.terminate()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

