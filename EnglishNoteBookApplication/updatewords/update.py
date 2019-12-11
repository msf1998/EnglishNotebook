from utill.db import Database
from model.word import Word
class UpdateWord(object):
    """修改单词的释义、例句"""
    def __init__(self):
        db = Database()
        self.__con = db.getConnect()
    def updateAWord(self,word):
        '''接受一个Word对象，修改数据库中的原单词，返回受影响的行数'''
        cur = self.__con.cursor()
        result = cur.execute("update words set translation = %s, example = %s where word = %s",(word.getTrans(),word.getExample(),word.getWord()))
        self.__con.commit()
        return result


