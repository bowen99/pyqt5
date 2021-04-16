from pywinauto.keyboard import send_keys
from pywinauto import Application
from datetime import datetime
import time
import pyautogui
import pyperclip
import os

app = Application().start(r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe")
        # pyperclip.copy("C:\Program Files (x86)\Tencent\WeChat\WeChat.exe")
app = Application().connect(path=r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe")

# send_keys('^f')
# pyperclip.copy('汪狗')
# send_keys('^v')
# send_keys('~')
