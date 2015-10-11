#-*- coding: utf-8 -*-
#mysqldb
#coding:utf-8
#函数动能：分类
import time
import datetime
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
import MySQLdb as md
import mysql.connector
import pdb
class delete_Not_today():
    def deleteNumber(self,today,pastday):
        conn=mysql.connector.connect(user="root",password="lcy492",database="spiderdb",charset='utf8')
        cur=conn.cursor()
        sql="delete from spiderdb.security where time not in('%s','%s')"%(today,pastday);
        print sql         
        cur.execute(sql)
        conn.commit()
        conn.close()
localtime=time.strftime("%Y-%m-%d", time.localtime())
localtime1=time.strftime("%Y-%m-%d", time.localtime(time.time()-24*60*60))
print localtime,localtime1
a=delete_Not_today()
a.deleteNumber(localtime,localtime1)


