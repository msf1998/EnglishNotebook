from selectwords.select import SelectFromDB
sfdb = SelectFromDB()
print(sfdb.selectTenWords(101,'character'))
print(sfdb.selectTenWords(0,'addtime'))