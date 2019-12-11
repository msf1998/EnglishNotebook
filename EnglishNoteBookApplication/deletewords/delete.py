from utill.db import Database
from model.word import Word
class DeleteWord(object):
    """从数据库中删除一项单词数据,或者清除整个表，作者信息除外"""
    def __init__(self):
        db = Database()
        self.__con = db.getConnect()
    def deleteAWord(self,word):
        '''接受一个Word字符串，删除数据库中的原单词，返回受影响的行数'''
        cur = self.__con.cursor()
        try:
            result = cur.execute("delete from words where word = %s",(word,))
        except Exception as e:
            result = -1
        self.__con.commit()
        return result
    def deleteAll(self):
        '''清空整个单词表,作者信息除外'''
        cur = self.__con.cursor()
        result = cur.callproc("truncate_words",(0,))
        self.__con.commit()
        return result