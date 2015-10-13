import mysql.connector
class Truncate():
    def truncate(self):
        db=mysql.connector.connect(user='root',password='###',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        sql='TRUNCATE spiderdb.security'
        cursor.execute(sql)
        db.commit()
        db.close()
t=Truncate()
t.truncate()
