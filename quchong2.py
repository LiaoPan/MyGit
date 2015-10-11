#-*- coding: utf-8 -*-
import sys
import gensim
from gensim import corpora, models, similarities
import logging
sys.path.append('../')
import MySQLdb as md
import mysql.connector
import pdb
import jieba
import jieba.analyse
from optparse import OptionParser
class GetTitle():
    def getContent(self):
        db=mysql.connector.connect(user='root',password='lcy492',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='select content from spiderdb.security'               
        try:
            cursor.execute(sql)
            data=cursor.fetchall()
            for row in data:
                Content.append("".join(row))
        except:
            print "Error:unable to fetch data"
        finally:
            return Content
    def getTitle(self):
        db=mysql.connector.connect(user='root',password='lcy492',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='select title from spiderdb.security'            
        try:
            cursor.execute(sql)
            data=cursor.fetchall()
            for row in data:
                Content.append("".join(row))
        except:
            print "Error:unable to fetch data"
        finally:
            return Content
    def modifyContent(self,i):
        conn=mysql.connector.connect(user="root",password="lcy492",database="spiderdb",charset='utf8')
        cur=conn.cursor()
        sql="update spiderdb.security SET title='null'  where id='%d'"%(i)
        print sql                
        cur.execute(sql) 
        conn.commit()  
        conn.close()
    def deleteContent(self):
        conn=mysql.connector.connect(user="root",password="lcy492",database="spiderdb",charset='utf8')
        cur=conn.cursor()     
        sql="delete from spiderdb.security where title='null'"
        print sql         
        cur.execute(sql)
        conn.commit()  
        conn.close()
    def saveWeight(self,e,j):
        conn=mysql.connector.connect(user="root",password="lcy492",database="spiderdb",charset='utf8')
        cur=conn.cursor()
        sql="update spiderdb.security SET weight='%s'  where id='%d'"%(e,j)
        print sql                
        cur.execute(sql) 
        conn.commit()  
        conn.close()
a=GetTitle()
mytitle=a.getTitle()
mycontent=a.getContent()
texts=[]
i=0
for c in mycontent:
    if c:
        tags = jieba.analyse.extract_tags(c,10,False)
    else:
        tags = jieba.analyse.extract_tags(mytitle[i], 10,False)
    i=i+1   
    #print h
    texts.append(tags)
    #print(",".join(tags))
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)
dictionary = corpora.Dictionary(texts)    
corpus = [dictionary.doc2bow(text) for text in texts]
#print corpus
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
print 'ok'
#for doc in corpus_tfidf:
    #print doc
#print tfidf.dfs
#print tfidf.idfs
index = similarities.MatrixSimilarity(corpus_tfidf)
#for doc in index:
    #print doc
#print index
sims = index[corpus_tfidf]
#print sims
similarity = list(sims)
#j为行的索引，k为列的索引
e=0
j=0
for t in similarity:
    k=0
    for s in t:
        if s>=0.29491:
        #if s>=4:
            if k>j:
                e=e+1
                print s,j,k
                a=GetTitle()
                a.modifyContent(k+1)
                a.deleteContent()
        k=k+1
    j=j+1
    print j,e
    b=GetTitle()
    b.saveWeight(e,j)
    e=0
