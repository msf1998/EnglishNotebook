from updatewords.update import UpdateWord
from model.word import Word
word = Word()
word.setWord(input("请输入单词：\n"))
word.setTrans(input("请输入中文释义：\n"))
word.setExample(input("请输入例句：\n"))
ud = UpdateWord()
print(ud.updateAWord(word))