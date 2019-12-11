from utill.db import Database
class SelectFromDB:
    '''从数据库中获取需要的单词数据，包括一次选出多个（10个）或者筛选出指定的单词'''
    def __init__(self):
        db = Database()
        self.__con = db.getConnect()
    def selectTenWords(self,n,order):
        '''接受一个int参数，表示页数（0-n），一个字符串参数，表示排序规则（character表示按照字典顺序排序，addtime表示按照添加时间排序）。
        返回一个元组，元组中的每一项也是一个元组，包括单词、释义、例句'''
        cur = self.__con.cursor()
        cur.execute("select count(*) from words")
        count = int(cur.fetchone()[0])
        mp = 0
        if count%10 ==0:
            mp = count//10
        else:
            mp = count//10 + 1
        n = (n % mp) * 10
        if order == 'character':
            cur.execute("select word,translation,example from view_words_word limit " + str(n) + ",10",)
        else:
            cur.execute("select word,translation,example from view_words_addtime limit " + str(n) + ",10")
        result = cur.fetchall()
        cur.close()
        return result
    def selectAWord(self,word):
        '''接受一个单词字符串，以元组形式返回该单词在数据库中的记录'''
        cur = self.__con.cursor()
        cur.execute("select word,translation,example from words where word = %s",[word])
        result = cur.fetchone()
        cur.close()
        return result