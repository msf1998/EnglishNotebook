from utill.db import Database
from model.word import Word
from utill.excel import readExcel
class InsertDB:
    '''向数据库中插入数据，可以一个一个插入，也可以导入txt文件或者excel文件批量插入'''
    def __init__(self):
        '''初始化数据库连接'''
        database = Database()
        self.__con = database.getConnect()
    def addWord(self,word):
        '''接受一个单词对象，然后插入到数据库中，返回数据库中改变的行数'''
        cur = self.__con.cursor()
        result = cur.execute("insert into words(word,translation,example) values(%s,%s,%s)",(word.getWord(),word.getTrans(),word.getExample()))
        self.__con.commit()
        cur.close()
        return result
    def addwords(self,path):
        '''接受一个txt文件或者excel文件的路径字符串，向数据库批量导入单词，然后返回数据库中改变的行数'''
        cur = self.__con.cursor()
        if path.endswith(".txt"):
            #导入txt文件
            result = cur.execute("load data local infile '" + path + "' into table words")
            self.__con.commit()
        elif path.endswith(".xlsx"):
            #导入excel文件
            result = 0
            words = readExcel(path)
            for word in words:
                n = cur.execute("insert into words(word,translation,example) values(%s,%s,%s)",word)
                self.__con.commit()
                result += n
        else:
            result = -1
        cur.close()
        return result
    def __del__(self):
        self.__con.close()

