from windows.mainwindow import MainWindowFact
from tkinter import *
def indexWindow():
    mwf = MainWindowFact()
    mw = mwf.createMainWindow(800,500)
    label = Label(mw,text = "Welcome To English Notebook",font = ("宋体",25))
    label.pack()
    mwf.run()