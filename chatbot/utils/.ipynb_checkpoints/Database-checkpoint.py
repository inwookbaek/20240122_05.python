# DB제어모듈
import pymysql
import pymysql.cursors
import logging

class Database:
    '''
        Chatbot의 Database 제어 모듈...
    '''
    def __init(self, host, user, password, db_name, charset='utf8'):
        slef.host = host
        slef.user = user
        slef.password = password
        slef.db_name = db_name
        slef.charset = charset
        slef.conn = None
        
    def connect(self):
        if self.conn != None: return

        self.conn = pymysql.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            db = self.db_name,
            charset = self.charset   
        )
        
    def close(self):
        if self.conn is None: return

        if not self.conn.open:
            self.conn = None
            return

        self.conn.close()
        self.conn = None

    # insert, delete, update
    def execute(self, sql):
        last_row_id = -1
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
            self.conn.commit()
            last_row_id = cursor.lastrowid
            logging.debug("execute last_row_is : %d", last_row_id) 
        except Exception as e:
            logging.error(e)    

    def select_one(self, sql):
        result = None
        try:
            with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
        except Exception as e:
           logging.error(e)
        finally:
            return result

    def select_all(self, sql):
        result = None
        try:
            with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
        except Exception as e:
           logging.error(e)
        finally:
            return result        
