import threading
import json

from chatbot.config.DatabaseConfig import *
from chatbot.utils.Database import Database
from chatbot.utils.BotServer import BotServer
from chatbot.utils.Preprocess import Preprocess
from chatbot.models.intent.IntentModel import IntentModel
from chatbot.models.ner.NerModel import NerModel
from chatbot.utils.FindAnswer import FindAnswer

# 1. 전처리
p = Preprocess(word2index_dic='./chatbot/train_tools/dict/chatbot_dict.bin'
               , userdic='./chatbot/utils/user_dic.tsv')

# 2. 의도파악학습모델
intent = IntentModel(model_name='./chatbot/models/intent/intent_model.keras', preprocess=p)

# 3. 개체인식학습모델
ner = NerModel(model_name='./chatbot/models/ner/ner_model.keras', preprocess=p)

# 4. 클라이언트가 연결되는 순간 실행되는 Thread함수
#    적절한 답변을 검색한후에 요청(requext)한 클라이언트에 응답(response)
def to_client(conn, addr, params):
    db = params['db']

    try:
        db.connect()

        # 1) data 수신(발화자의 질의)
        # conn은 쳇봇클라이언트의 소캣객체, recv()메서드는 데이터의
        # 수신이 완료될 때까지 블럭킹, 최대 2048bytes만큼 데이터를 수신
        # 에러(연결중단 or 예외)가 있을 경우에 recv()메서드는 None을 리턴
        read = conn.recv(2048)  # 수신데이터가 있을 때 까지 블럭킹
        print('='*60)
        print(f'Connection from : {str(addr)}') # localhost:5000?....

        if read is None or not read: # 클라이언트연결중단 or 에러가 있을 겨우
            print('Client Connection Stop!!')
            exit(0)
        
        # 2) json형태로 변환
        recv_json_data = json.loads(read.decode())
        print(f'데이터수신 : {recv_json_data}')
        query = recv_json_data['Query']
        
        # 3) 발화자의 의도파악
        intent_predict = intent.predict_class(query)
        intent_name = intent.labels[intent_predict]
    
        # 4) 개체명 인식
        ner_predicts = ner.predict(query)
        ner_tags = ner.predict_tags(query)

        # 5) DB에서 답변검색
        try:
            f = FindAnswer(db)
            answer_text, answer_image = f.search(intent_name, ner_tags)
            answer = f.tag_to_word(ner_predicts, answer_text)
        except Exception as e:
            print(e)
            answer = "죄송합니다. 무슨 말인지 모르겠어요! 조금 더 학습을 할게요 ㅠㅠ"
            answer_image = None

        send_json_data_str = {
            "Query": query,
            "Answer": answer,
            "AnswerImageUrl": answer_image,
            "Intent": intent_name,
            "NER": ner_tags   
        }

        message = json.dumps(send_json_data_str)
        conn.send(message.encode())
        
    except Exception as e:
        print(e)
    finally:
        if db is not None:
            db.close()

# 5. chatbot application start
if __name__ == '__main__':
    
    # 1) 답변검색을 위한 DB 연결
    db = Database(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db_name=DB_NAME)
    print('DB Connection Successful!!')

    port = 5050
    listen = 100

    # 2) 쳇봇서버동작 - 챗봇클라이언트 연결을 대기(무한 loop)
    bot = BotServer(port, listen)
    bot.create_socket()
    print('ChatBot Server Start!!')

    while True:
        conn, addr = bot.ready_for_client()
        params = {
            'db': db
        }

        client = threading.Thread(target=to_client, args=(conn, addr, params))
        client.start()
