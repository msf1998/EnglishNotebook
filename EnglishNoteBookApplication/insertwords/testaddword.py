from insertwords.insert import InsertDB
from model.word import Word
word = Word()
word.setWord(input("请输入单词：\n"))
word.setTrans(input("请输入汉语释义：\n"))
word.setExample(input("请输入例句：\n"))
indb = InsertDB()
print(indb.addWord(word))