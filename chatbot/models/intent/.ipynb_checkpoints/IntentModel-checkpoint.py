# 쳇봇엔진 - 의도분류모델로딩(모델재사용)
import tensorflow as tf
from tensorflow.keras.models import Model, load_model
from tensorflow.keras import preprocessing

# 의도분류모델모듈
class IntentModel:

    # 1) 생성자
    def __init__(self, model_name, preprocess):
        # 의도클래스레이블
        self.labels = {0:'인사', 1:'욕설', 2:'주문', 3:'예약', 4:'기타'}

        # 훈련된 의도분류모델 로딩
        self.model = load_model(model_name)

        # chatbot.Preprocess
        self.p = preprocess

    # 2) 의도클래스 예측함수
    def predict_class(self, query):
        # 1) 형태소분석
        pos = self.p.pos(query)

        # 2) 문장(query)내에서 키워드추출, 불용어제거
        keywords = self.p.get_keywords(pos, without_tag=True)
        sequences = [self.p.get_wordidx_sequence(keywords)]

        # 3) 벡터의 최대크기
        from chatbot.config.GlobalParams import MAX_SEQ_LEN
        
        # 4) 패딩처리
        padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')

        # 5) 예측
        predict = self.model.predict(padded_seqs)
        predict_class = tf.math.argmax(predict, axis=1)

        # 6) 예측결과 즉, 의도클래스를 반환
        return predict_class.numpy()[0]
