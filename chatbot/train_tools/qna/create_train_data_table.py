import pymysql
from chatbot.config. DatabaseConfig import *

db = None

try:
    db = pymysql.connect(
        host = DB_HOST, 
        port = DB_PORT,
        user = DB_USER, 
        passwd = DB_PASSWORD,
        db = DB_NAME,
        charset = 'utf8'
    )

    # 테이블생성 sql 정의
    sql = '''
        create table if not exists chatbot_train_data (
            id            int unsigned not null auto_increment,
            intent        varchar(45),
            ner           varchar(1024),
            query         text null,
            answer        text not null,
            answer_image  varchar(2048) null,
            primary key (id)
        )
        engine = InnoDB default charset=utf8
    '''

    # 테이블생성
    with db.cursor() as cursor:
        cursor.execute(sql)
except Exception as e:
    print(e)
finally:
    if db is not None:
        db.close()
