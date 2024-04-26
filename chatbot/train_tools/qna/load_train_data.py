import pymysql
import openpyxl
from chatbot.config.DatabaseConfig import *

# 학습데이터초기화
def all_clear_train_data(db):
    # 기존 학습 데이터 삭제
    sql = 'delete from chatbot_train_data'
    with db.cursor() as cursor:
        cursor.execute(sql)

    
# db에 데이터저장
def insert_data(db, xls_row):
    intent, ner, query, answer, answer_image_url = xls_row
    sql = '''
        insert chatbot_train_data(intent, ner, query, answer, answer_image) 
        values('%s','%s','%s','%s','%s')
    ''' % (intent.value, ner.value, query.value, answer.value, answer_image_url.value)

    # 엑셀에서 불러온 cell에 데이터가 없을 경우 Null로 치환
    sql = sql.replace("None", "null")
    
    with db.cursor() as cursor:
        cursor.execute(sql)  
        print(f'{query.value}이 성공적으로 저장되었습니다!!')
        db.commit()

train_file = './chatbot/train_tools/qna/train_data.xlsx'

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

    # 기존 학습데이터 초기화
    all_clear_train_data(db)

    # train_data.xls데이터 업로드
    wb = openpyxl.load_workbook(train_file)
    sheet = wb['Sheet1']

    for row in sheet.iter_rows(min_row=2): # header행은 skip
        insert_data(db, row) # 데이터저장
except Exception as e:
    print(e)
finally:
    if db is not None:
        db.close()
