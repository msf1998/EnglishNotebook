from xml.dom.minidom import parse
import MySQLdb
class Database:
    '''读取dbconfig.xml文件，建立数据库连接'''
    def __init__(self):
        '''读取dbconfig.xml配置文件,获取host,port,db,user,passwd,charset信息'''
        dom = parse("dbconfig.xml")
        domelement = dom.documentElement
        dbconfig_list = domelement.getElementsByTagName("dbinfo")
        host_list = dbconfig_list[0].getElementsByTagName("host");
        self.___host = host_list[0].childNodes[0].data
        port_list = dbconfig_list[0].getElementsByTagName("port")
        self.__port = int(port_list[0].childNodes[0].data)
        db_list = dbconfig_list[0].getElementsByTagName("db")
        self.__db = db_list[0].childNodes[0].data
        user_list = dbconfig_list[0].getElementsByTagName("user")
        self.__user = user_list[0].childNodes[0].data
        passwd_list = dbconfig_list[0].getElementsByTagName("passwd")
        self.__passwd = passwd_list[0].childNodes[0].data
        charset_list = dbconfig_list[0].getElementsByTagName("charset")
        self.__charset = charset_list[0].childNodes[0].data

    def getConnect(self):
        '''返回一个数据库连接'''
        con = MySQLdb.connect(host = self.___host,db = self.__db, user = self.__user, passwd = self.__passwd, port = self.__port, charset = self.__charset)
        return con