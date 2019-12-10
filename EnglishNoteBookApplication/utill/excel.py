import xlrd

def readExcel(path):
    '''接受一个excel文件的路径字符串，返回一个包含excel表中全部数据的列表对象'''
    workbook = xlrd.open_workbook(path)
    table = workbook.sheet_by_index(0)
    n = table.nrows
    words = list()
    for i in range(n):
        words.append(table.row_values(i))
    return words
