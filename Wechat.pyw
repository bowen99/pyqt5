# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'company.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(582, 397)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(160, 100, 245, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 582, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.domain)
        self.pushButton_2.clicked.connect(self.desktop)
        self.pushButton_3.clicked.connect(self.mail)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def domain(self):
        def copy(str):
            pyperclip.copy(str)
            pyautogui.hotkey('ctrl', 'v')

        def hotkey(x, y, *args):
            pyautogui.hotkey(x, y)

        def send_key(str):
            '''
            ^ --> Ctrl
            % --> Alt
            '''
            send_keys(str)

        def press(x):
            pyautogui.press(x)

        def domm():
            hotkey('win', 'r')
            copy(dom)
            press('enter')
            hotkey('alt', 'c')
            hotkey('alt', 'd')
            press('tab')
            copy(domname)
            press('enter')
            time.sleep(4)
            copy(name)
            press('tab')
            copy(passwd)
            press('enter')
            time.sleep(3)
            press('enter')
            time.sleep(3)
            press('enter')
        domm()
    def desktop(self):
        def copy(str):
            pyperclip.copy(str)
            pyautogui.hotkey('ctrl', 'v')

        def hotkey(x, y, *args):
            pyautogui.hotkey(x, y)

        def send_key(str):
            '''
            ^ --> Ctrl
            % --> Alt
            '''
            send_keys(str)

        def press(x):
            pyautogui.press(x)

        def de():
            hotkey('win', 'r')
            copy(desk)
            press('enter')
            # time.sleep(3)
            hotkey('alt', 'm')
            # time.sleep(0.5)
            hotkey('alt', 'U')
            # time.sleep(0.5)
            hotkey('alt', 'N')
            # time.sleep(0.5)
            hotkey('alt', 'R')
            press('enter')
        de()
    def mail(self):
        def ma():
            def copy(str):
                pyperclip.copy(str)
                pyautogui.hotkey('ctrl', 'v')

            def hotkey(x, y, *args):
                pyautogui.hotkey(x, y)

            def send_key(str):
                '''
                ^ --> Ctrl
                % --> Alt
                '''
                send_keys(str)

            def press(x):
                pyautogui.press(x)
            hotkey('win', 'r')
            copy(email)
            press('enter')
            send_key('%D')
            press('shift')
            pyautogui.typewrite('123')
            press('enter')
            press('enter')
            press('enter')
            hotkey('alt', 'r')
            hotkey('alt', 'f')
            hotkey('alt', 'a')
            send_key('%D')
            if not exists(mail_address):
                makedirs(mail_address)
            copy(mail_address)


            # send_key('^v')
            hotkey('shift', 'enter')
            hotkey('alt', 'n')
            copy(mouth)
            press('enter')
            hotkey('alt', 'd')
            hotkey('alt', 'y')
            press('left')
            hotkey('alt', 'f')
            hotkey('alt', 'y')
            press('enter')
            hotkey('alt', 'c')
            hotkey('alt', 'c')
            press('enter')
        ma()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Domain"))
        self.pushButton_2.setText(_translate("MainWindow", "DeskTop"))
        self.pushButton_3.setText(_translate("MainWindow", "Mail"))
if __name__ == '__main__':
    import pyautogui
    import pyperclip
    import time
    from datetime import datetime
    from pywinauto import Application
    from pywinauto.keyboard import send_keys
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtWidgets import QApplication, QMainWindow
    import sys
    from os.path import exists
    from os import makedirs
    pyautogui.PAUSE = 2
    pyautogui.FAILSAFE = True
    desk = "rundll32.exe shell32.dll,Control_RunDLL desk.cpl,,0"
    dom = "C:\Windows\System32\SystemPropertiesComputerName.exe"
    domname = "sz.fic.com.tw"
    name = "adddomain"
    passwd = "MisB130"
    email = "D:\software\office\Office14\MLCFG32.CPL"
    # email = "C:\PROGRA~2\MICROS~1\Office14\MLCFG32.CPL"
    mail_address = "d:\mail"
    m = datetime.now()
    mouth = m.strftime('%Y%m%d')
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())