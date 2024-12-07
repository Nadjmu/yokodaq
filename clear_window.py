from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication

import os

class Ui_clear(object):
    
    def clearTemp(self):
        print("hi")
        os.remove("tempp.csv")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200,120)
        MainWindow.setStyleSheet("background-color: rgb(255,255,255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.warning = QtWidgets.QLabel(self.centralwidget)
        self.warning.setGeometry(QtCore.QRect(30,30,140,16))
        self.warning.setObjectName("warning")
        self.warning.setStyleSheet("background-color: rgb(0, 0, 127);color:rgb(255,255,255)")
        
        self.bt1 = QtWidgets.QPushButton(self.centralwidget)
        self.bt1.setGeometry(QtCore.QRect(40,70,20,20))
        self.bt1.setObjectName("bt1")
        self.bt1.clicked.connect(self.clearTemp)
        self.bt1.clicked.connect(MainWindow.close)
        
        self.bt2 = QtWidgets.QPushButton(self.centralwidget)
        self.bt2.setGeometry(QtCore.QRect(140,70,20,20))
        self.bt2.setObjectName("bt2")
        self.bt2.clicked.connect(MainWindow.close)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        #self.retranslateUi(MainWindow)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #self.warning.setText(_translate("MainWindow","Are you sure about that"))
        MainWindow.setWindowTitle(_translate("MainWindow", "Warning"))
        self.warning.setText(_translate("MainWindow","   Are you sure about that?"))
        self.bt1.setText(_translate("MainWindow","Yes"))
        self.bt2.setText(_translate("MainWindow","No"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_clear()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())