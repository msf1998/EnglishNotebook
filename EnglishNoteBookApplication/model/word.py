class Word(object):
    """word的简单对象类"""
    def setWord(self,word):
        self.__word = word
    def setTrans(self,trans):
        self.__trans = trans
    def setExample(self,example):
        self.__example = example
    def getWord(self):
        return self.__word
    def getTrans(self):
        return self.__trans
    def getExample(self):
        return self.__example


