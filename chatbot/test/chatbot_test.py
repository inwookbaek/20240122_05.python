# chatbot엔진 동작 테스트하기
from chatbot.config.DatabaseConfig import *
from chatbot.utils.Database import Database
from chatbot.utils.Preprocess import Preprocess

# 1. 전처리객체생성
p = Preprocess(word2index_dic='./chatbot/train_tools/dict/chatbot_dict.bin'
               , userdic='./chatbot/utils/user_dic.tsv')

# 2. DB객체생성
db = Database(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db_name=DB_NAME)
db.connect()

# 3. 발화자질의
query = '오전에 탕수육 10개를 주문합니다'
# query = '오전에 탕수육  주문합니다'
# query = '화자의 질문의도를 파악합니다.'
# query = '안녕하세요'
# query = '자장면 주문할게요'

# 4. 발화자의도파악
from chatbot.models.intent.IntentModel import IntentModel
intent = IntentModel(model_name='./chatbot/models/intent/intent_model.keras', preprocess=p)
predict = intent.predict_class(query)
intent_name = intent.labels[predict]

# 5. 개체명인식
from chatbot.models.ner.NerModel import NerModel
ner = NerModel(model_name='./chatbot/models/ner/ner_model.keras', preprocess=p)
predicts = ner.predict(query)
ner_tags = ner.predict_tags(query)

# 6. 출력확인
print(f'발화자의 질의 = {predict}')
print(f'발화자의 의도 = {intent_name}')
print(f'발화자의 질의의 개체명 = {predicts}')
print(f'발화자의 질의의 NER태그(답변검색에 필요한 NER태그) = {ner_tags}')

# 7. 답변검색
from chatbot.utils.FindAnswer import FindAnswer

try:
    f = FindAnswer(db)
    # print(f.make_query(intent_name, ner_tags))
    answer_text, answer_image = f.search(intent_name, ner_tags)
    answer = f.tag_to_word(predicts, answer_text)
except Exception as e:
    print(e)
    answer = "죄송합니다. 무슨 말인지 모르겠어요!"

print(f'답변검색결과 = {answer}')

db.close()
