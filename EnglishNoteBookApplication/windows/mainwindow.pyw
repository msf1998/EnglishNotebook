from tkinter import *
def new_window():
    win2 = Tk()

class MainWindowFact:
    '''此类创建的对象主要用来产生一个主窗口对象并提供时使这个窗口对象产生作用的方法'''
    def createMainWindow(self,x,y):
        '''接受两个int类型的参数x、y，返回一个长为x高为y的窗口'''
        self.__win = Tk()
        self.__win.title("English Notebook")
        self.__win.geometry(str(x) + "x" + str(y))

        #创建菜单
        #创建一个菜单栏
        menubar = Menu(self.__win)
        #创建“添加”菜单
        addmenu = Menu(menubar,tearoff = 0)
        #将addmenu添加到菜单栏并取名为“添加”
        menubar.add_cascade(menu = addmenu,label = '添加')
        #向addemenu中添加下拉菜单项，同时绑定相应函数
        addmenu.add_command(label = "手动输入",command = new_window)
        addmenu.add_separator()#添加分割线
        #添加二级菜单
        importmenu = Menu(addmenu,tearoff = 0)
        addmenu.add_cascade(menu = importmenu,label = "文件导入",underline = 0)
        #添加二级菜单的菜单项
        importmenu.add_command(label = "导入txt文件",command = new_window)
        importmenu.add_separator()
        importmenu.add_command(label = "导入excel文件",command = new_window)

        #添加“学习”菜单
        studymenu = Menu(menubar,tearoff = 0)
        menubar.add_cascade(menu = studymenu,label = "学习")
        #为studymenu添加菜单项
        studymenu.add_command(label = "学习单词",command = new_window)

        #添加“搜索”菜单
        searchmenu = Menu(menubar,tearoff = 0)
        menubar.add_cascade(menu = searchmenu,label = "搜索")
        #添加菜单项
        searchmenu.add_command(label = "查单词",command = new_window)

        #添加“帮助”菜单
        helpmenu = Menu(menubar,tearoff = 0)
        menubar.add_cascade(menu = helpmenu,label = "帮助")
        #添加菜单项
        helpmenu.add_command(label = "关于",command = new_window)
        helpmenu.add_separator()
        helpmenu.add_command(label = "退出",command = self.__win.quit) 

        #将菜单栏添加到主窗口
        self.__win.config(menu = menubar)

        return self.__win
    def run(self):
        '''接受一个窗口对象，然后使此对象产生作用'''

        self.__win.mainloop()
        try:
            self.__win.destroy()  #解决tKinter的quit对导致程序卡死，无法关闭的问题
        except Exception as e:
            a = 1