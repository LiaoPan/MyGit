#-*- coding: utf-8 -*-

#mysqldb
#coding:utf-8
#函数动能：分类
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
import MySQLdb as md
import mysql.connector
import pdb
from tgrocery import Grocery
grocery=Grocery('trydb')

#连接数据库，取出训练集
#'v'代表漏洞，'h'代表病毒木马，'f'代表国外资讯，'c'代表国内资讯，'g'代表国内政策，'m'代表会议，s代表技术，‘o'代表其他,
class GetContent():
    def getContent(self):	    
        db = mysql.connector.connect(user="root",password="###",database="###",charset='utf8')	   
        cursor = db.cursor()
        Content = []  		
        sql = "select content from spiderdb.dictionary"   

        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            for row in data:               
                Content.append("".join(row))		
        except:
            print "Error: unable to fetch data1"
        finally:
            return Content
    def getContent1(self):	    
        db = mysql.connector.connect(user="root",password="###",database="spiderdb",charset='utf8')	   
        cursor = db.cursor()
        Content = []  		
        sql = "select content from spiderdb.security"   
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            for row in data:
                Content.append("".join(row)) 			
        except:
            print "Error: unable to fetch data2"
        finally:
            return Content

    def getSign(self):	    
        db = mysql.connector.connect(user="root",password="###",database="spiderdb",charset='utf8')	   
        cursor = db.cursor()
        Content = []  		
        sql = "select sign from spiderdb.dictionary"   
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            for row in data:
                Content.append("".join(row))		
        except:
            print "Error: unable to fetch data4"
        finally:
            return Content

    def getTitle(self):	    
        db = mysql.connector.connect(user="root",password="###",database="spiderdb",charset='utf8')	   
        cursor = db.cursor()
        Content = []  		
        sql = "select title from spiderdb.dictionary"
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            for row in data:               
                Content.append("".join(row))		
        except:
            print "Error: unable to fetch data6"
        finally:
            return Content
    def getTitle1(self):	    
        db = mysql.connector.connect(user="root",password="###",database="spiderdb",charset='utf8')	   
        cursor = db.cursor()
        Content = []  		
        sql = "select title from spiderdb.security"
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            for row in data:
                Content.append("".join(row))			
        except:
            print "Error: unable to fetch data7"
        finally:
            return Content

    def saveContent(self,i,num):
        conn=mysql.connector.connect(user="root",password="###",database="spiderdb",charset='utf8')
        cur=conn.cursor()
        sql="update  security SET sign ='%s' where id='%d'"%(num,i)
        print sql         
       
        cur.execute(sql)
      
        conn.commit()
        conn.close()
    def deleteNULL(self):
        conn=mysql.connector.connect(user="root",password="###",database="spiderdb",charset='utf8')
        cur=conn.cursor()
        sql="update  security SET content='' where content='NULL'"
        print sql         
        cur.execute(sql)
        conn.commit()
        conn.close()  
message=GetContent()
message.deleteNULL()
#m代表从数据库中选到的内容,t为预测之后的结果
#如果内容是存在的，就根据内容进行预测，如果内容不存在，就根据title来进行预测
mycontent=message.getContent()
mytitle=message.getTitle()
mysign=message.getSign()
train_list=[]
train_listc=[]
i=0
q=0
for c in mycontent:
    if c:
        k=mysign[q]
        p=[k,c]
        train_listc.append(p)
        q=q+1

for t in mytitle:
    m=mysign[i]
    n=[m,t]
    train_list.append(n)
    i=i+1
grocery.train(train_listc)
grocery.train(train_list)
grocery.save()
new_grocery=Grocery('trydb')
new_grocery.load()
pc=message.getContent1()
pt=message.getTitle1()
g=1
for newscontent in pc:
    if newscontent:
        num=new_grocery.predict(newscontent+pt[g-1])
        message.saveContent(g,num)
    else:
        num=new_grocery.predict(pt[g-1])
        message.saveContent(g,num)
   
    g=g+1
